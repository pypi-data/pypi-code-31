# Copyright 2017-2018 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

import logging
import os
import re
import shlex
import subprocess
import sys
import time

import daemonize

import guild.plugin
import guild.run

from guild import config
from guild import deps
from guild import op_util
from guild import opref
from guild import util
from guild import var

log = logging.getLogger("guild")

OP_RUNFILE_PATHS = [
    ["org_click"],
    ["org_psutil"],
    ["guild", "external"],
]
PROC_TERM_TIMEOUT_SECONDS = 30
SIGTERM_EXIT_STATUS = -15

NO_ARG_VALUE = object()

class InvalidMain(ValueError):
    pass

class Operation(object):

    def __init__(self, model_ref, opdef, run_dir=None, resource_config=None,
                 extra_attrs=None, stage_only=False, gpus=None):
        self.model_ref = model_ref
        self.opdef = opdef
        (self.cmd_args,
         self.flag_vals,
         self._flag_map) = _init_cmd_args(opdef)
        self.cmd_env = _init_cmd_env(opdef, gpus)
        self._run_dir = run_dir
        self.resource_config = resource_config or {}
        self.extra_attrs = extra_attrs
        self.stage_only = stage_only
        self.gpus = gpus
        self._started = None
        self._stopped = None
        self._run = None
        self._proc = None
        self._exit_status = None

    @property
    def run_dir(self):
        return self._run_dir or (self._run.path if self._run else None)

    def run(self, quiet=False, background_pidfile=None):
        self.init()
        self.resolve_deps()
        return self.proc(quiet, background_pidfile)

    def init(self):
        self._init_run()
        self._init_attrs()

    def _init_run(self):
        self._run = init_run(self._run_dir)
        log.debug("initializing run in %s", self._run.path)
        self._run.init_skel()

    def _init_attrs(self):
        assert self._run is not None
        self._started = guild.run.timestamp()
        self._run.write_attr("opref", self._opref_attr(), raw=True)
        _delete_pending(self._run)
        self._run.write_attr("started", self._started)
        for name, val in (self.extra_attrs or {}).items():
            self._run.write_attr(name, val)
        self._run.write_attr("flags", self.opdef.flag_values())
        self._run.write_attr("cmd", self.cmd_args)
        if self._flag_map:
            self._run.write_attr("_flag_map", self._flag_map)
        for key, val in self.opdef.modeldef.extra.items():
            self._run.write_attr("_extra_%s" % key, val)

    def _opref_attr(self):
        ref = opref.OpRef.from_op(self.opdef.name, self.model_ref)
        return str(ref)

    def resolve_deps(self):
        assert self._run is not None
        ctx = deps.ResolutionContext(
            target_dir=self._run.path,
            opdef=self.opdef,
            resource_config=self.resource_config)
        resolved = deps.resolve(self.opdef.dependencies, ctx)
        self._run.write_attr("deps", _sort_resolved(resolved))
        self._maybe_write_label(resolved)

    def _maybe_write_label(self, resolved):
        if "label" in self.extra_attrs or not self.opdef.label:
            return
        label = _format_label(
            self.opdef.label,
            self.flag_vals,
            self.resource_config,
            resolved)
        self._run.write_attr("label", label)

    def proc(self, quiet=False, background_pidfile=None):
        self._pre_proc()
        if self.stage_only:
            self._stage_proc()
        else:
            if background_pidfile:
                self._background_proc(background_pidfile, quiet)
            else:
                return self._foreground_proc(quiet)

    def _background_proc(self, pidfile, quiet):
        action = lambda: self._foreground_proc(quiet)
        daemon = daemonize.Daemonize(app="guild_op", action=action, pid=pidfile)
        if not quiet:
            log.info("Operation started in background (pidfile is %s)", pidfile)
        daemon.start()

    def _foreground_proc(self, quiet):
        self._start_proc()
        self._wait_for_proc(quiet)
        self._finalize_attrs()
        return self._exit_status

    def _pre_proc(self):
        if not self.opdef.pre_process:
            return
        cmd = self.opdef.pre_process.strip().replace("\n", " ")
        cwd = self._run.path
        # env init order matters - we want _proc_env() to take
        # precedence over _cmd_arg_env()
        env = _cmd_arg_env(self.cmd_args)
        env.update(self._proc_env())
        log.debug("pre-process command: %s", cmd)
        log.debug("pre-process env: %s", env)
        log.debug("pre-process cwd: %s", cwd)
        subprocess.check_call(cmd, shell=True, env=env, cwd=cwd)

    def _stage_proc(self):
        env = self._proc_env()
        _write_sourceable_env(env, self._run.guild_path("env"))
        log.debug("operation command: %s", self.cmd_args)
        log.debug("operation env: %s", env)

    def _start_proc(self):
        assert self._proc is None
        assert self._run is not None
        args = self.cmd_args
        env = self._proc_env()
        self._run.write_attr("env", env)
        cwd = self._run.path
        log.debug("starting operation run %s", self._run.id)
        log.debug("operation command: %s", args)
        log.debug("operation env: %s", env)
        log.debug("operation cwd: %s", cwd)
        self._proc = subprocess.Popen(
            args,
            env=env,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        _write_proc_lock(self._proc, self._run)

    def _proc_env(self):
        assert self._run is not None
        env = dict(self.cmd_env)
        env["RUN_DIR"] = self._run.path
        env["RUN_ID"] = self._run.id
        return env

    def _wait_for_proc(self, quiet):
        assert self._proc is not None
        try:
            proc_exit_status = self._watch_proc(quiet)
        except KeyboardInterrupt:
            proc_exit_status = self._handle_proc_interrupt()
        self._exit_status = _op_exit_status(proc_exit_status, self.opdef)
        self._stopped = guild.run.timestamp()
        _delete_proc_lock(self._run)

    def _watch_proc(self, quiet):
        assert self._proc is not None
        output = op_util.RunOutput(self._run, self._proc, quiet)
        exit_status = self._proc.wait()
        output.wait_and_close()
        return exit_status

    def _handle_proc_interrupt(self):
        log.info("Operation interrupted - waiting for process to exit")
        kill_after = time.time() + PROC_TERM_TIMEOUT_SECONDS
        while time.time() < kill_after:
            if self._proc.poll() is not None:
                break
            time.sleep(1)
        if self._proc.poll() is None:
            log.warning("Operation process did not exit - stopping forcefully")
            util.kill_process_tree(self._proc.pid, force=True)
        return SIGTERM_EXIT_STATUS

    def _finalize_attrs(self):
        assert self._run is not None
        assert self._exit_status is not None
        assert self._stopped is not None
        if not os.path.exists(self._run.path):
            log.warning(
                "run directory has been deleted, unable to finalize")
            return
        if not os.path.exists(self._run._guild_dir):
            log.warning(
                "run Guild directory has been deleted, unable to finalize")
            return
        self._run.write_attr("exit_status", self._exit_status)
        self._run.write_attr("stopped", self._stopped)

def _init_cmd_args(opdef):
    python_args = [_python_cmd(opdef), "-um", "guild.op_main"]
    flag_vals = _resolved_flag_vals(opdef.flag_values())
    try:
        cmd_args = _cmd_args(opdef.main, flag_vals)
    except guild.util.UndefinedReferenceError as e:
        raise InvalidMain(opdef.main, "undefined reference '%s'" % e)
    else:
        flag_args, flag_map = _flag_args(flag_vals, opdef, cmd_args)
        cmd_args = python_args + cmd_args + flag_args
        return cmd_args, flag_vals, flag_map

def _python_cmd(_opdef):
    # TODO: This is an important operation that should be controlled
    # by the model (e.g. does it run under Python 2 or 3, etc.) and
    # not by whatever Python runtime is configured in the user env.
    return sys.executable

def _resolved_flag_vals(flag_vals):
    return util.resolve_all_refs(flag_vals)

def _cmd_args(main, flag_vals):
    def format_part(part):
        return str(util.resolve_refs(part, flag_vals))
    return [format_part(part) for part in _split_main(main)]

def _split_main(main):
    if isinstance(main, list):
        return main
    else:
        # If main is None, this call will block (see
        # https://bugs.python.org/issue27775)
        if not main:
            raise InvalidMain("", "missing command spec")
        return shlex.split(main or "")

def _flag_args(flag_vals, opdef, cmd_args):
    flag_args = []
    flag_vals, flag_map = _flag_cmd_arg_vals(flag_vals, opdef)
    cmd_options = _cmd_options(cmd_args)
    for name in sorted(flag_vals):
        value = flag_vals[name]
        if name in cmd_options:
            log.warning(
                "ignoring flag '%s = %s' because it's shadowed "
                "in the operation cmd", name, value)
            continue
        flag_args.extend(_cmd_option_args(name, value))
    return flag_args, flag_map

def _flag_cmd_arg_vals(flag_vals, opdef):
    vals = {}
    flag_map = {}
    for name, val in flag_vals.items():
        if val is None:
            continue
        flagdef = opdef.get_flagdef(name)
        if flagdef:
            if flagdef.choices:
                _apply_choice_args(flagdef, val, flag_vals, vals)
            if not flagdef.arg_skip:
                _apply_flag_arg(flagdef, val, flag_vals, vals, flag_map)
        else:
            vals[name] = val
    return vals, flag_map

def _apply_choice_args(flagdef, val, flag_vals, target):
    for choice in flagdef.choices:
        if choice.value == val:
            if choice.args:
                args = {
                    name: util.resolve_refs(val, flag_vals)
                    for name, val in choice.args.items()
                }
                target.update(args)
            break
    else:
        log.warning(
            "unsupported choice %r for '%s' flag, ignoring",
            val, flagdef.name)

def _apply_flag_arg(flagdef, value, flag_vals, target, flag_map):
    if flagdef.arg_name:
        arg_name = flagdef.arg_name
        flag_map[arg_name] = flagdef.name
    else:
        arg_name = flagdef.name
    arg_val = util.resolve_refs(value, flag_vals)
    if flagdef.arg_switch is not None:
        if arg_val == flagdef.arg_switch:
            target[arg_name] = NO_ARG_VALUE
    else:
        target[arg_name] = arg_val

def _cmd_options(args):
    p = re.compile("--([^=]+)")
    return [m.group(1) for m in [p.match(arg) for arg in args] if m]

def _cmd_option_args(name, val):
    opt = "--%s" % name
    if val is None:
        return []
    elif val is NO_ARG_VALUE:
        return [opt]
    else:
        return [opt, str(val)]

def _init_cmd_env(opdef, gpus):
    env = util.safe_osenv()
    env.update(opdef.env)
    env["GUILD_HOME"] = config.guild_home()
    env["GUILD_OP"] = opdef.fullname
    env["GUILD_PLUGINS"] = _op_plugins(opdef)
    env["LOG_LEVEL"] = str(logging.getLogger().getEffectiveLevel())
    env["PYTHONPATH"] = _python_path(opdef)
    # SCRIPT_DIR is inserted by op_main at sys.path[0] - use empty string
    # here to include run dir first in sys.path
    env["SCRIPT_DIR"] = ""
    # CMD_DIR is where the operation cmd was run
    env["CMD_DIR"] = os.getcwd()
    env["MODEL_DIR"] = opdef.guildfile.dir
    env["MODEL_PATH"] = os.path.pathsep.join(_model_paths(opdef))
    if opdef.set_trace:
        env["SET_TRACE"] = "1"
    if opdef.handle_keyboard_interrupt:
        env["HANDLE_KEYBOARD_INTERRUPT"] = "1"
    util.apply_env(env, os.environ, ["PROFILE"])
    if gpus is not None:
        log.info(
            "Limiting available GPUs (CUDA_VISIBLE_DEVICES) to: %s",
            gpus or "<none>")
        env["CUDA_VISIBLE_DEVICES"] = gpus
    return env

def _cmd_arg_env(args):
    op_main_pos = args.index("guild.op_main")
    assert op_main_pos != -1
    flags = op_util.args_to_flags(args[op_main_pos+1:])
    return {
        name.upper(): str(val)
        for name, val in flags.items()
    }

def _op_plugins(opdef):
    op_plugins = []
    for name, plugin in guild.plugin.iter_plugins():
        if _plugin_disabled_in_project(name, opdef):
            plugin_enabled = False
            reason = "explicitly disabled by model or user config"
        else:
            plugin_enabled, reason = plugin.enabled_for_op(opdef)
        log.debug(
            "plugin '%s' %s%s",
            name,
            "enabled" if plugin_enabled else "disabled",
            " (%s)" % reason if reason else "")
        if plugin_enabled:
            op_plugins.append(name)
    return ",".join(sorted(op_plugins))

def _plugin_disabled_in_project(name, opdef):
    disabled = (opdef.disabled_plugins +
                opdef.modeldef.disabled_plugins)
    return any([disabled_name in (name, "all") for disabled_name in disabled])

def _python_path(opdef):
    paths = (
        _env_paths() +
        _model_paths(opdef) +
        _guild_paths()
    )
    return os.path.pathsep.join(paths)

def _env_paths():
    env = os.getenv("PYTHONPATH")
    return env.split(os.path.pathsep) if env else []

def _model_paths(opdef):
    return _opdef_paths(opdef) + _model_parent_paths(opdef.modeldef)

def _opdef_paths(opdef):
    if not opdef.guildfile.dir:
        return []
    abs_gf_dir = os.path.abspath(opdef.guildfile.dir)
    if opdef.python_path is not None:
        return [os.path.join(abs_gf_dir, p) for p in opdef.python_path]
    return [abs_gf_dir]

def _model_parent_paths(modeldef):
    return [os.path.abspath(parent.dir) for parent in modeldef.parents]

def _guild_paths():
    guild_path = os.path.dirname(os.path.dirname(__file__))
    abs_guild_path = os.path.abspath(guild_path)
    return [abs_guild_path] + _runfile_paths()

def _runfile_paths():
    return [
        os.path.abspath(path)
        for path in sys.path if _is_runfile_pkg(path)
    ]

def _is_runfile_pkg(path):
    for runfile_path in OP_RUNFILE_PATHS:
        split_path = path.split(os.path.sep)
        if split_path[-len(runfile_path):] == runfile_path:
            return True
    return False

def _write_sourceable_env(env, dest):
    skip_env = ("PWD", "_")
    with open(dest, "w") as out:
        for name in sorted(env):
            if name in skip_env:
                continue
            out.write("export {}='{}'\n".format(name, env[name]))

def _write_proc_lock(proc, run):
    with open(run.guild_path("LOCK"), "w") as f:
        f.write(str(proc.pid))

def _op_exit_status(proc_exit_status, opdef):
    if proc_exit_status == SIGTERM_EXIT_STATUS and opdef.stoppable:
        return 0
    return proc_exit_status

def _delete_proc_lock(run):
    try:
        os.remove(run.guild_path("LOCK"))
    except OSError:
        pass

def _delete_pending(run):
    try:
        os.remove(run.guild_path("PENDING"))
    except OSError:
        pass

def init_run(path=None):
    if not path:
        run_id = guild.run.mkid()
        path = os.path.join(var.runs_dir(), run_id)
    else:
        run_id = os.path.basename(path)
    return guild.run.Run(run_id, path)

def _format_label(template, flag_vals, resource_config, resolved_deps):
    vals = _init_label_val_lookup(flag_vals, resource_config, resolved_deps)
    return util.render_label(template, vals)

def _init_label_val_lookup(flag_vals, resource_config, resolved_deps):
    lookup = {}
    # List in reverse order of precedence.
    lookup.update(resource_config)
    lookup.update(_resolved_dep_label_vals(resolved_deps))
    lookup.update(flag_vals)
    return lookup

def _resolved_dep_label_vals(deps):
    return {name: _dep_label(deps[name]) for name in deps}

def _dep_label(dep_files):
    # Use first file to infer dependency label.
    if not dep_files:
        return "#unknown#"
    return util.find_apply([_run_id_label, _file_label], dep_files[0])

def _run_id_label(path):
    run_id_m = re.search(r".guild[/\\]runs/(.+?)[/\\]", path)
    if run_id_m:
        return run_id_m.group(1)[:8]
    return None

def _file_label(path):
    return os.path.basename(path)

def _sort_resolved(resolved):
    return {
        name: sorted(files) for name, files in resolved.items()
    }
