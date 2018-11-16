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

import copy
import errno
import logging
import os
import re
import sys

import six
import yaml

from guild import resourcedef
from guild import util

log = logging.getLogger("guild")

NAMES = ["guild.yml"]

ALL_TYPES = [
    "config",
    "include",
    "model",
    "package",
    "test",
]

MODEL_TYPES = ["model", "config"]

_cache = {}

###################################################################
# Exceptions
###################################################################

class GuildfileError(Exception):

    def __init__(self, guildfile_or_path, msg):
        super(GuildfileError, self).__init__(guildfile_or_path, msg)
        if isinstance(guildfile_or_path, Guildfile):
            self.path = guildfile_or_path.src
        else:
            self.path = guildfile_or_path
        self.msg = msg

    def __str__(self):
        return "error in %s: %s" % (self.path, self.msg)

class NoModels(GuildfileError):

    def __init__(self, guildfile_or_path):
        super(NoModels, self).__init__(guildfile_or_path, "no models")

    def __str__(self):
        return "no models in %s" % self.path

class GuildfileReferenceError(GuildfileError):
    pass

class GuildfileCycleError(GuildfileError):

    def __init__(self, guildfile_or_path, desc, cycle):
        msg = "%s (%s)" % (desc, " -> ".join(cycle))
        super(GuildfileCycleError, self).__init__(guildfile_or_path, msg)

class GuildfileIncludeError(GuildfileError):

    def __init__(self, guildfile_or_path, include):
        msg = (
            "cannot find include '%s' "
            "(includes must be local to including Guild file or a "
            "Guild package on the system path)" % include)
        super(GuildfileIncludeError, self).__init__(guildfile_or_path, msg)

###################################################################
# Helpers
###################################################################

def _required(name, data, guildfile):
    try:
        return data[name]
    except KeyError:
        raise GuildfileError(
            guildfile,
            "missing required '%s' attribute in %r"
            % (name, data))

def _string_source(src):
    return re.match(r"<.*>$", src)

###################################################################
# Guildfile
###################################################################

class Guildfile(object):

    def __init__(self, data, src=None, dir=None, included=None,
                 extends_seen=None):
        if not dir and src and not _string_source(src):
            dir = os.path.dirname(src)
        if src is None and dir is None:
            raise ValueError("either src or dir must be specified")
        self.src = src
        self.dir = dir
        self.models = {}
        self.package = None
        self.tests = []
        coerced = _coerce_guildfile_data(data, self)
        self.data = self._expand_data_includes(coerced, included or [])
        try:
            self._apply_data(extends_seen or [])
        except (GuildfileError, resourcedef.ResourceFormatError):
            raise
        except Exception as e:
            log.error("loading %s: %r", self.src, e)
            raise

    def _expand_data_includes(self, data, included):
        i = 0
        while i < len(data):
            item = data[i]
            try:
                includes = item["include"]
            except KeyError:
                i += 1
            else:
                new_items = self._include_data(includes, included)
                data[i:i+1] = new_items
                i += len(new_items)
        return data

    def _include_data(self, includes, included):
        if not _string_source(self.src):
            included.append(os.path.abspath(self.src))
        include_data = []
        for path in includes:
            path = self._find_include(path)
            if path in included:
                raise GuildfileCycleError(
                    "cycle in 'includes'",
                    included[0],
                    included + [path])
            data = yaml.load(open(path, "r"))
            guildfile = Guildfile(data, path, included=included)
            include_data.extend(guildfile.data)
        return include_data

    def _find_include(self, include):
        path = util.find_apply(
            [self._local_include,
             self._sys_path_include,
             self._gpkg_include],
            include)
        if path:
            return path
        raise GuildfileIncludeError(self, include)

    def _local_include(self, path):
        log.debug("looking for include '%s' in %s", path, self.dir)
        full_path = os.path.abspath(os.path.join(self.dir or "", path))
        if os.path.exists(full_path):
            log.debug("found include %s", full_path)
            return full_path
        return None

    @staticmethod
    def _sys_path_include(include):
        include_path = include.replace(".", os.path.sep)
        for path in sys.path:
            log.debug("looking for include '%s' in %s", include, path)
            for name in NAMES:
                guildfile = os.path.join(path, include_path, name)
                if os.path.exists(guildfile):
                    log.debug("found include %s", guildfile)
                    return guildfile
        return None

    def _gpkg_include(self, include):
        return self._sys_path_include("gpkg." + include)

    def _apply_data(self, extends_seen):
        for item in self.data:
            item_type, name = self._validated_item_type(item)
            if item_type == "model":
                self._apply_model(name, item, extends_seen)
            elif item_type == "package":
                self._apply_package(name, item)
            elif item_type == "test":
                self._apply_test(name, item)

    def _validated_item_type(self, item):
        used = [name for name in ALL_TYPES if name in item]
        if not used:
            raise GuildfileError(
                self, ("missing required type (one of: %s) in %r"
                       % (", ".join(ALL_TYPES), item)))
        elif len(used) > 1:
            raise GuildfileError(
                self, ("multiple types (%s) in %r"
                       % (", ".join(used), item)))
        validated_type = used[0]
        name = item[validated_type]
        if not isinstance(name, six.string_types):
            raise GuildfileError(
                self, ("invalid %s name: %r"
                       % (validated_type, name)))
        return validated_type, name

    def _apply_model(self, name, data, extends_seen):
        if name in self.models:
            raise GuildfileError(self, "duplicate model '%s'" % name)
        model = ModelDef(name, data, self, extends_seen)
        self.models[name] = model

    def _apply_package(self, name, data):
        if self.package:
            raise GuildfileError(self, "mutiple package definitions")
        self.package = PackageDef(name, data, self)

    def _apply_test(self, name, data):
        self.tests.append(TestDef(name, data, self))

    @property
    def default_model(self):
        models = list(self.models.values())
        if len(models) == 1:
            return models[0]
        for m in models:
            if m.default:
                return m
        return None

    def get_test(self, name):
        for t in self.tests:
            if t.name == name:
                return t
        raise ValueError(name)

    def __repr__(self):
        return "<guild.guildfile.Guildfile '%s'>" % self

    def __str__(self):
        return self.src or self.dir

    def __eq__(self, _x):
        raise AssertionError()

###################################################################
# Coercion rules
###################################################################

def _coerce_guildfile_data(data, guildfile):
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise GuildfileError(guildfile, "invalid guildfile data: %r" % data)
    return [
        _coerce_guildfile_item_data(item_data, guildfile)
        for item_data in data]

def _coerce_guildfile_item_data(data, guildfile):
    if not isinstance(data, dict):
        return data
    return {
        name: _coerce_top_level_attr(name, val, guildfile)
        for name, val in data.items()
    }

def _coerce_top_level_attr(name, val, guildfile):
    if name == "include":
        return _coerce_include(val, guildfile)
    elif name == "extends":
        return _coerce_extends(val, guildfile)
    elif name == "operations":
        return _coerce_operations(val, guildfile)
    elif name == "flags":
        return _coerce_flags(val, guildfile)
    else:
        return val

def _coerce_include(data, guildfile):
    return _coerce_string_to_list(data, guildfile, "include")

def _coerce_extends(data, guildfile):
    return _coerce_string_to_list(data, guildfile, "extends")

def _coerce_operations(data, guildfile):
    if not isinstance(data, dict):
        raise GuildfileError(guildfile, "invalid operations value: %r" % data)
    return {
        op_name: _coerce_operation(op, guildfile)
        for op_name, op in data.items()
    }

def _coerce_operation(data, guildfile):
    if isinstance(data, six.string_types):
        return {
            "main": data
        }
    return {
        name: _coerce_operation_attr(name, val, guildfile)
        for name, val in data.items()
    }

def _coerce_operation_attr(name, val, guildfile):
    if name == "flags":
        return _coerce_flags(val, guildfile)
    elif name == "python-path":
        return _coerce_op_python_path(val, guildfile)
    else:
        return val

def _coerce_flags(data, guildfile):
    if not isinstance(data, dict):
        raise GuildfileError(guildfile, "invalid flags value: %r" % data)
    return {
        name: _coerce_flag(name, val, guildfile)
        for name, val in data.items()
    }

def _coerce_flag(name, data, guildfile):
    if name.startswith("$"):
        return data
    elif isinstance(data, dict):
        return data
    elif isinstance(data, six.string_types + (int, float, bool)):
        return {"default": data}
    elif data is None:
        return {"default": None}
    else:
        raise GuildfileError(guildfile, "invalid flag value: %r" % data)

def _coerce_op_python_path(data, guildfile):
    if data is None:
        return None
    return _coerce_string_to_list(data, guildfile, "python-path")

def _coerce_string_to_list(data, guildfile, name):
    if isinstance(data, six.string_types):
        return [data]
    elif isinstance(data, list):
        return data
    else:
        raise GuildfileError(
            guildfile,
            "invalid %s value: %r" % (name, data))

###################################################################
# Include attribute support
###################################################################

def _resolve_includes(data, section_name, guildfiles):
    assert isinstance(data, dict), data
    resolved = {}
    seen_includes = set()
    section_data = data.get(section_name) or {}
    _apply_section_data(
        section_data,
        guildfiles,
        section_name,
        seen_includes,
        resolved)
    return resolved

def _apply_section_data(data, guildfile_path, section_name,
                        seen_includes, resolved):
    for name in _includes_first(data):
        if name == "$include":
            includes = _coerce_includes(data[name], guildfile_path[0])
            _apply_includes(
                includes,
                guildfile_path,
                section_name,
                seen_includes,
                resolved)
        else:
            _apply_data(
                name,
                data[name],
                resolved)

def _coerce_includes(val, src):
    return _coerce_string_to_list(val, src, "$include")

def _apply_includes(includes, guildfile_path, section_name,
                    seen_includes, resolved):
    _assert_guildfile_data(guildfile_path[0])
    for ref in includes:
        if ref in seen_includes:
            break
        seen_includes.add(ref)
        # Have to access guildfile.data here rather than use
        # guildfile.get because guildfile may not be initialized at
        # this point.
        include_model, include_op = _split_include_ref(ref, guildfile_path[0])
        include_data = _find_include_data(
            include_model,
            include_op,
            section_name,
            guildfile_path)
        if include_data is None:
            raise GuildfileReferenceError(
                guildfile_path[0],
                "invalid include reference '%s'" % ref)
        _apply_section_data(
            include_data,
            guildfile_path,
            section_name,
            seen_includes,
            resolved)

def _assert_guildfile_data(guildfile):
    # This is called by guildfile components that need to access
    # guildfile data before the modefile is fully initialized.
    assert hasattr(guildfile, "data"), "modesfile data not initialized"

def _split_include_ref(ref, src):
    parts = ref.split(":", 1)
    if len(parts) == 1:
        return parts[0], None
    else:
        if not parts[0]:
            raise GuildfileReferenceError(
                src, ("invalid include reference '%s': operation references "
                      "must be specified as MODEL:OPERATION" % ref))
        return parts

def _find_include_data(model_name, op_name, section_name, guildfile_path):
    for guildfile in guildfile_path:
        for top_level_data in guildfile.data:
            if _item_name(top_level_data, MODEL_TYPES) == model_name:
                if op_name:
                    op_data = _op_data(top_level_data, op_name)
                    if op_data is None:
                        continue
                    return op_data.get(section_name) or {}
                else:
                    return top_level_data.get(section_name) or {}
    return None

def _item_name(data, types):
    for attr in types:
        try:
            return data[attr]
        except KeyError:
            pass
    return None

def _op_data(model_data, op_name):
    return model_data.get("operations", {}).get(op_name)

def _includes_first(names):
    return sorted(names, key=lambda x: "\x00" if x == "$include" else x)

def _apply_data(name, data, resolved):
    try:
        cur = resolved[name]
    except KeyError:
        new = {}
        new.update(data)
        resolved[name] = new
    else:
        _apply_missing_vals(cur, data)

def _apply_missing_vals(target, source):
    assert isinstance(target, dict), target
    assert isinstance(source, dict), source
    for name in source:
        target[name] = source[name]

###################################################################
# Model def
###################################################################

class ModelDef(object):

    def __init__(self, name, data, guildfile, extends_seen=None):
        data = _extended_data(data, guildfile, extends_seen or [])
        self.name = name
        self.guildfile = guildfile
        self.parents = _dedup_parents(data.get("__parents__", []))
        self.description = (data.get("description") or "").strip()
        self.references = data.get("references") or []
        self.operations = _init_ops(data, self)
        self.resources = _init_resources(data, self)
        self.disabled_plugins = data.get("disabled-plugins") or []
        self.extra = data.get("extra") or {}
        self.default = data.get("default", False)

    @property
    def guildfile_path(self):
        return [self.guildfile] + self.parents

    def __repr__(self):
        return "<guild.guildfile.ModelDef '%s'>" % self.name

    def get_operation(self, name):
        for op in self.operations:
            if op.name == name:
                return op
        return None

    def get_resource(self, name):
        for res in self.resources:
            if res.name == name:
                return res
        return None

def _extended_data(config_data, guildfile, seen=None, resolve_params=True):
    data = copy.deepcopy(config_data)
    extends = config_data.get("extends") or []
    if extends:
        _apply_parents_data(extends, guildfile, seen, data)
    if resolve_params:
        data = _resolve_param_refs(data, _params(data))
    return data

def _params(data):
    params = data.get("params") or {}
    return {
        name: _resolve_param(name, params)
        for name in params
    }

def _resolve_param(name, params):
    iter_count = 0
    seen = set()
    val = str(params[name])
    seen.add(val)
    # Resolve val until we get a value that we've already seen (either
    # fully resolved or a cycle). Use iter counter to guard against
    # non-terminating loops.
    while iter_count < 100:
        val = _resolve_str_param_refs(val, params)
        if val in seen:
            return val
        seen.add(val)
        iter_count += 1
    assert False, (name, params)

def _apply_parents_data(extends, guildfile, seen, data):
    for name in extends:
        if name in seen:
            raise GuildfileCycleError(
                guildfile,
                "cycle in 'extends'",
                seen + [name])
        parent = _parent_data(name, guildfile, seen)
        inheritable = [
            "description",
            "extra",
            "flags",
            "operations",
            "params",
            "references",
            "resources",
        ]
        _apply_parent_pkg_guildfile(parent, data)
        _apply_parent_data(parent, data, inheritable)

def _parent_data(name, guildfile, seen):
    if "/" in name:
        return _pkg_parent_data(name, guildfile, seen)
    else:
        return _guildfile_parent_data(name, guildfile, seen)

def _pkg_parent_data(name, guildfile, seen):
    pkg, model_name = name.split("/", 1)
    if not model_name:
        raise GuildfileReferenceError(
            guildfile,
            "invalid model or config reference '%s': "
            "missing model name" % name)
    pkg_guildfile_path = _find_pkg_guildfile(pkg)
    if not pkg_guildfile_path:
        raise GuildfileReferenceError(
            guildfile, "cannot find Guild file for package '%s'" % pkg)
    pkg_guildfile = from_file(pkg_guildfile_path, seen + [name])
    parent_data = _modeldef_data(model_name, pkg_guildfile)
    if parent_data is None:
        raise GuildfileReferenceError(
            guildfile,
            "undefined model or config '%s' in package '%s'"
            % (model_name, pkg))
    parent_data["__pkg_guildfile__"] = pkg_guildfile
    return _extended_data(parent_data, pkg_guildfile, seen + [name], False)

def _modeldef_data(name, guildfile):
    for item in guildfile.data:
        if _item_name(item, MODEL_TYPES) == name:
            return item
    return None

def _find_pkg_guildfile(pkg):
    pkg_path = pkg.replace("-", "_").replace(".", os.path.sep)
    for path in sys.path:
        log.debug("looking for pkg '%s' in %s", pkg, path)
        for name in NAMES:
            guildfile = os.path.join(path, pkg_path, name)
            if os.path.exists(guildfile):
                log.debug("found pkg Guild file %s", guildfile)
                return guildfile
    return None

def _guildfile_parent_data(name, guildfile, seen):
    parent_data = _modeldef_data(name, guildfile)
    if parent_data is None:
        raise GuildfileReferenceError(
            guildfile, "undefined model or config '%s'" % name)
    return _extended_data(parent_data, guildfile, seen + [name], False)

def _apply_parent_pkg_guildfile(parent, child):
    parents = parent.get("__parents__", [])
    try:
        parent_pkg_guildfile = parent["__pkg_guildfile__"]
    except KeyError:
        pass
    else:
        parents.append(parent_pkg_guildfile)
    child.setdefault("__parents__", []).extend(parents)

def _apply_parent_data(parent, child, attrs=None):
    if not isinstance(parent, dict) or not isinstance(child, dict):
        return
    for name, parent_val in parent.items():
        if attrs is not None and name not in attrs:
            continue
        try:
            child_val = child[name]
        except KeyError:
            _apply_value(child, name, parent_val)
        else:
            _apply_parent_data(parent_val, child_val)

def _apply_value(target, name, val):
    target[name] = copy.deepcopy(val)

def _resolve_param_refs(val, params):
    if isinstance(val, dict):
        return _resolve_dict_param_refs(val, params)
    elif isinstance(val, list):
        return _resolve_list_param_refs(val, params)
    elif isinstance(val, six.string_types):
        return _resolve_str_param_refs(val, params)
    else:
        return val

def _resolve_dict_param_refs(d, params):
    return {
        name: _resolve_param_refs(val, params)
        for name, val in d.items()
    }

def _resolve_list_param_refs(l, params):
    return [_resolve_param_refs(x, params) for x in l]

def _resolve_str_param_refs(s, params):
    parts = [
        part for part in
        re.split(r"({{.+?}})", str(s))
        if part != ""]
    resolved = [_resolve_param_ref(part, params) for part in parts]
    if len(resolved) == 1:
        return resolved[0]
    else:
        return "".join([str(part) for part in resolved])

def _resolve_param_ref(val, params):
    if val.startswith("{{") and val.endswith("}}"):
        ref_name = val[2:-2]
        try:
            ref_val = params[ref_name]
        except KeyError:
            pass
        else:
            val = ref_val
    return val

def _dedup_parents(parents):
    seen = set()
    deduped = []
    for parent in parents:
        if parent.dir in seen:
            continue
        deduped.append(parent)
        seen.add(parent.dir)
    return deduped

def _init_ops(data, modeldef):
    ops_data = data.get("operations") or {}
    return [
        OpDef(key, ops_data[key], modeldef)
        for key in sorted(ops_data)
    ]

def _init_resources(data, modeldef):
    data = _resolve_includes(data, "resources", modeldef.guildfile_path)
    return [ResourceDef(key, data[key], modeldef) for key in sorted(data)]

###################################################################
# Op def
###################################################################

class OpDef(object):

    def __init__(self, name, data, modeldef):
        if not isinstance(data, dict):
            raise GuildfileError(
                modeldef.guildfile,
                "invalid operation def: %r" % data)
        self.modeldef = modeldef
        self.flags = _init_flags(data, self)
        self._flag_vals = _init_flag_values(self.flags)
        self.guildfile = modeldef.guildfile
        self.name = name
        self.description = (data.get("description") or "").strip()
        self.main = data.get("main")
        self.python_path = data.get("python-path")
        self.env = data.get("env") or {}
        self.plugin_op = data.get("plugin-op")
        self.disabled_plugins = data.get("disabled-plugins") or []
        self.dependencies = _init_dependencies(data.get("requires"), self)
        self.pre_process = data.get("pre-process")
        self.remote = data.get("remote") or False
        self.stoppable = data.get("stoppable") or False
        self.set_trace = data.get("set-trace") or False
        self.label = data.get("label")
        self.handle_keyboard_interrupt = (
            data.get("handle-keyboard-interrupt") or False)

    def __repr__(self):
        return "<guild.guildfile.OpDef '%s'>" % self.fullname

    @property
    def fullname(self):
        return "%s:%s" % (self.modeldef.name, self.name)

    def get_flagdef(self, name):
        for flag in self.flags:
            if flag.name == name:
                return flag
        return None

    def flag_values(self, include_none=True):
        return dict(self._iter_flag_values(include_none))

    def _iter_flag_values(self, include_none):
        for name, val in self._flag_vals.items():
            if val is not None or include_none:
                yield name, val

    def set_flag_value(self, name, val):
        self._flag_vals[name] = val

    def get_flag_value(self, name, default=None):
        try:
            return self._flag_vals[name]
        except KeyError:
            return default

    def update_flags(self, flag_host):
        merged_map = {flag.name: flag for flag in self.flags}
        merged_map.update({flag.name: flag for flag in flag_host.flags})
        merged_flags = [merged_map[name] for name in sorted(merged_map)]
        merged_vals = {}
        merged_vals.update(self._flag_vals)
        merged_vals.update(flag_host.flag_values())
        self.flags = merged_flags
        self._flag_vals = merged_vals

    def update_dependencies(self, opdef):
        self.dependencies.extend(opdef.dependencies)

def _init_flags(data, opdef):
    data = _resolve_includes(data, "flags", opdef.modeldef.guildfile_path)
    return [FlagDef(name, data[name], opdef) for name in sorted(data)]

class FlagDef(object):

    def __init__(self, name, data, opdef):
        self.name = name
        self.opdef = opdef
        self.default = data.get("default")
        self.description = data.get("description") or ""
        self.type = data.get("type")
        self.required = bool(data.get("required"))
        self.arg_name = data.get("arg-name")
        self.arg_skip = bool(data.get("arg-skip"))
        self.arg_switch = data.get("arg-switch")
        self.choices = _init_flag_choices(data.get("choices"), self)
        self.null_label = data.get("null-label")

    def __repr__(self):
        return "<guild.guildfile.FlagDef '%s'>" % self.name

def _init_flag_values(flagdefs):
    return {
        flag.name: flag.default
        for flag in flagdefs
    }

def _init_flag_choices(data, flagdef):
    if not data:
        return []
    return [FlagChoice(choice_data, flagdef) for choice_data in data]

class FlagChoice(object):

    def __init__(self, data, flagdef):
        self.flagdef = flagdef
        if isinstance(data, dict):
            self.value = data.get("value")
            self.description = data.get("description") or ""
            self.args = data.get("args") or {}
        else:
            self.value = data
            self.description = ""
            self.args = {}

def _init_dependencies(requires, opdef):
    if not requires:
        return []
    if isinstance(requires, six.string_types):
        requires = [requires]
    return [OpDependency(data, opdef) for data in requires]

class OpDependency(object):

    def __init__(self, data, opdef):
        self.opdef = opdef
        if isinstance(data, six.string_types):
            self.spec = data
            self.description = ""
        elif isinstance(data, dict):
            self.spec = _required("resource", data, self.opdef.guildfile)
            self.description = data.get("description") or ""
        else:
            raise GuildfileError(
                self, "invalid dependency value: %r" % data)

    def __repr__(self):
        return "<guild.guildfile.OpDependency '%s'>" % self.spec

class NoSuchResourceError(ValueError):

    def __init__(self, name, dep):
        super(NoSuchResourceError, self).__init__(
            "resource '%s' is not defined in model '%s'"
            % (name, dep.opdef.modeldef.name))
        self.resource_name = name
        self.dependency = dep

###################################################################
# Resource def
###################################################################

class ResourceDef(resourcedef.ResourceDef):

    source_types = resourcedef.ResourceDef.source_types + ["operation"]

    def __init__(self, name, data, modeldef):
        fullname = "%s:%s" % (modeldef.name, name)
        super(ResourceDef, self).__init__(name, data, fullname)
        self.private = self.private
        self.modeldef = modeldef

    def get_source_resolver(self, source, resource):
        scheme = source.parsed_uri.scheme
        if scheme == "operation":
            from guild import resolver # expensive
            return resolver.OperationOutputResolver(
                source, resource, self.modeldef)
        else:
            return super(ResourceDef, self).get_source_resolver(
                source, resource)

    def _source_for_type(self, type, val, data):
        data = self._coerce_source_data(data)
        if type == "operation":
            return resourcedef.ResourceSource(
                self, "operation:%s" % val, **data)
        else:
            return super(ResourceDef, self)._source_for_type(type, val, data)

###################################################################
# Package def
###################################################################

DEFAULT_PKG_VERSION = "0.0.0"

class PackageDef(object):

    def __init__(self, name, data, guildfile):
        self.name = name
        self.guildfile = guildfile
        self.description = (data.get("description") or "").strip()
        self.version = data.get("version", DEFAULT_PKG_VERSION)
        self.url = data.get("url")
        self.author = data.get("author")
        self.author_email = data.get("author-email")
        self.license = data.get("license")
        self.tags = data.get("tags") or []
        self.python_tag = data.get("python-tag")
        self.data_files = data.get("data-files") or []
        self.python_requires = data.get("python-requires") or []
        self.requires = data.get("requires")
        self.packages = data.get("packages")

    def __repr__(self):
        return "<guild.guildfile.PackageDef '%s'>" % self.name

###################################################################
# Test def
###################################################################

class TestDef(object):

    def __init__(self, name, data, guildfile):
        self.name = name
        self.guildfile = guildfile
        self.description = (data.get("description") or "").strip()
        self.steps = data.get("steps") or []

    def __repr__(self):
        return "<guild.guildfile.TestDef '%s'>" % self.name

###################################################################
# Module API
###################################################################

def from_dir(path, filenames=None):
    log.debug("checking '%s' for model sources", path)
    filenames = NAMES if filenames is None else filenames
    for name in filenames:
        model_file = os.path.abspath(os.path.join(path, name))
        if os.path.isfile(model_file):
            log.debug("found model source '%s'", model_file)
            return from_file(model_file)
    raise NoModels(path)

def is_guildfile_dir(path):
    try:
        names = os.listdir(path)
    except OSError:
        names = []
    for name in names:
        if name in NAMES:
            return True
    return False

def from_file(src, extends_seen=None):
    cache_key = _cache_key(src)
    cached = _cache.get(cache_key)
    if cached:
        return cached
    _cache[cache_key] = mf = _load_guildfile(src, extends_seen)
    return mf

def _cache_key(src):
    return os.path.abspath(src)

def _load_guildfile(src, extends_seen):
    try:
        data = yaml.safe_load(open(src, "r"))
    except yaml.YAMLError as e:
        if log.getEffectiveLevel() <= logging.DEBUG:
            log.exception("loading yaml from %s", src)
        raise GuildfileError(src, str(e))
    else:
        return Guildfile(data, src, extends_seen=extends_seen)

def from_file_or_dir(src):
    try:
        return from_file(src)
    except IOError as e:
        if e.errno == errno.EISDIR:
            return from_dir(src)
        raise

def from_string(s, src="<string>"):
    return Guildfile(yaml.safe_load(s), src)
