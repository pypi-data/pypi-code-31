""" interactive debugging with PDB, the Python Debugger. """
from __future__ import absolute_import, division, print_function
import pdb
import sys
import os
from doctest import UnexpectedException

from _pytest.config import hookimpl

try:
    from builtins import breakpoint  # noqa

    SUPPORTS_BREAKPOINT_BUILTIN = True
except ImportError:
    SUPPORTS_BREAKPOINT_BUILTIN = False


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group._addoption(
        "--pdb",
        dest="usepdb",
        action="store_true",
        help="start the interactive Python debugger on errors or KeyboardInterrupt.",
    )
    group._addoption(
        "--pdbcls",
        dest="usepdb_cls",
        metavar="modulename:classname",
        help="start a custom interactive Python debugger on errors. "
        "For example: --pdbcls=IPython.terminal.debugger:TerminalPdb",
    )
    group._addoption(
        "--trace",
        dest="trace",
        action="store_true",
        help="Immediately break when running each test.",
    )


def pytest_configure(config):
    if config.getvalue("usepdb_cls"):
        modname, classname = config.getvalue("usepdb_cls").split(":")
        __import__(modname)
        pdb_cls = getattr(sys.modules[modname], classname)
    else:
        pdb_cls = pdb.Pdb

    if config.getvalue("trace"):
        config.pluginmanager.register(PdbTrace(), "pdbtrace")
    if config.getvalue("usepdb"):
        config.pluginmanager.register(PdbInvoke(), "pdbinvoke")

    # Use custom Pdb class set_trace instead of default Pdb on breakpoint() call
    if SUPPORTS_BREAKPOINT_BUILTIN:
        _environ_pythonbreakpoint = os.environ.get("PYTHONBREAKPOINT", "")
        if _environ_pythonbreakpoint == "":
            sys.breakpointhook = pytestPDB.set_trace

    old = (pdb.set_trace, pytestPDB._pluginmanager)

    def fin():
        pdb.set_trace, pytestPDB._pluginmanager = old
        pytestPDB._config = None
        pytestPDB._pdb_cls = pdb.Pdb
        if SUPPORTS_BREAKPOINT_BUILTIN:
            sys.breakpointhook = sys.__breakpointhook__

    pdb.set_trace = pytestPDB.set_trace
    pytestPDB._pluginmanager = config.pluginmanager
    pytestPDB._config = config
    pytestPDB._pdb_cls = pdb_cls
    config._cleanup.append(fin)


class pytestPDB(object):
    """ Pseudo PDB that defers to the real pdb. """

    _pluginmanager = None
    _config = None
    _pdb_cls = pdb.Pdb

    @classmethod
    def set_trace(cls, set_break=True):
        """ invoke PDB set_trace debugging, dropping any IO capturing. """
        import _pytest.config

        frame = sys._getframe().f_back
        if cls._pluginmanager is not None:
            capman = cls._pluginmanager.getplugin("capturemanager")
            if capman:
                capman.suspend_global_capture(in_=True)
            tw = _pytest.config.create_terminal_writer(cls._config)
            tw.line()
            tw.sep(">", "PDB set_trace (IO-capturing turned off)")
            cls._pluginmanager.hook.pytest_enter_pdb(config=cls._config)
        if set_break:
            cls._pdb_cls().set_trace(frame)


class PdbInvoke(object):
    def pytest_exception_interact(self, node, call, report):
        capman = node.config.pluginmanager.getplugin("capturemanager")
        if capman:
            out, err = capman.suspend_global_capture(in_=True)
            sys.stdout.write(out)
            sys.stdout.write(err)
        _enter_pdb(node, call.excinfo, report)

    def pytest_internalerror(self, excrepr, excinfo):
        for line in str(excrepr).split("\n"):
            sys.stderr.write("INTERNALERROR> %s\n" % line)
            sys.stderr.flush()
        tb = _postmortem_traceback(excinfo)
        post_mortem(tb)


class PdbTrace(object):
    @hookimpl(hookwrapper=True)
    def pytest_pyfunc_call(self, pyfuncitem):
        _test_pytest_function(pyfuncitem)
        yield


def _test_pytest_function(pyfuncitem):
    pytestPDB.set_trace(set_break=False)
    testfunction = pyfuncitem.obj
    pyfuncitem.obj = pdb.runcall
    if pyfuncitem._isyieldedfunction():
        arg_list = list(pyfuncitem._args)
        arg_list.insert(0, testfunction)
        pyfuncitem._args = tuple(arg_list)
    else:
        if "func" in pyfuncitem._fixtureinfo.argnames:
            raise ValueError("--trace can't be used with a fixture named func!")
        pyfuncitem.funcargs["func"] = testfunction
        new_list = list(pyfuncitem._fixtureinfo.argnames)
        new_list.append("func")
        pyfuncitem._fixtureinfo.argnames = tuple(new_list)


def _enter_pdb(node, excinfo, rep):
    # XXX we re-use the TerminalReporter's terminalwriter
    # because this seems to avoid some encoding related troubles
    # for not completely clear reasons.
    tw = node.config.pluginmanager.getplugin("terminalreporter")._tw
    tw.line()

    showcapture = node.config.option.showcapture

    for sectionname, content in (
        ("stdout", rep.capstdout),
        ("stderr", rep.capstderr),
        ("log", rep.caplog),
    ):
        if showcapture in (sectionname, "all") and content:
            tw.sep(">", "captured " + sectionname)
            if content[-1:] == "\n":
                content = content[:-1]
            tw.line(content)

    tw.sep(">", "traceback")
    rep.toterminal(tw)
    tw.sep(">", "entering PDB")
    tb = _postmortem_traceback(excinfo)
    post_mortem(tb)
    rep._pdbshown = True
    return rep


def _postmortem_traceback(excinfo):
    if isinstance(excinfo.value, UnexpectedException):
        # A doctest.UnexpectedException is not useful for post_mortem.
        # Use the underlying exception instead:
        return excinfo.value.exc_info[2]
    else:
        return excinfo._excinfo[2]


def _find_last_non_hidden_frame(stack):
    i = max(0, len(stack) - 1)
    while i and stack[i][0].f_locals.get("__tracebackhide__", False):
        i -= 1
    return i


def post_mortem(t):
    class Pdb(pytestPDB._pdb_cls):
        def get_stack(self, f, t):
            stack, i = pdb.Pdb.get_stack(self, f, t)
            if f is None:
                i = _find_last_non_hidden_frame(stack)
            return stack, i

    p = Pdb()
    p.reset()
    p.interaction(None, t)
