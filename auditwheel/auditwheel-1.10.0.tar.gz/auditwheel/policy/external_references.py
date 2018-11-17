import re
import os
import json
import logging
from typing import Tuple, Dict, List, Set, Any

from elftools.elf.elffile import ELFFile  # type: ignore

from ..elfutils import is_subdir
from . import POLICY_PRIORITY_HIGHEST, load_policies

log = logging.getLogger(__name__)
LIBPYTHON_RE = re.compile('^libpython\d\.\dm?.so(.\d)*$')


def lddtree_external_references(lddtree: Dict, wheel_path: str):
    # XXX: Document the lddtree structure, or put it in something
    # more stable than a big nested dict
    policies = load_policies()

    def filter_libs(libs, whitelist):
        for lib in libs:
            if 'ld-linux' in lib:
                # always exclude ld-linux.so
                continue
            if LIBPYTHON_RE.match(lib):
                # always exclude libpythonXY
                continue
            if lib in whitelist:
                # exclude any libs in the whitelist
                continue
            yield lib

    def get_req_external(libs: Set[str], whitelist: Set[str]):
        # get all the required external libraries
        libs = libs.copy()
        reqs = set()
        while libs:
            lib = libs.pop()
            reqs.add(lib)
            for dep in filter_libs(lddtree['libs'][lib]['needed'], whitelist):
                if dep not in reqs:
                    libs.add(dep)
        return reqs

    ret = {}  # type: Dict[str, Dict[str, Any]]
    for p in policies:
        needed_external_libs = []  # type: List[str]

        if not (p['name'] == 'linux' and p['priority'] == 0):
            # special-case the generic linux platform here, because it
            # doesn't have a whitelist. or, you could say its
            # whitelist is the complete set of all libraries. so nothing
            # is considered "external" that needs to be copied in.
            whitelist = set(p['lib_whitelist'])
            needed_external_libs = get_req_external(
                set(filter_libs(lddtree['needed'], whitelist)),
                whitelist)  # type: List[str]

        pol_ext_deps = {}
        for lib in needed_external_libs:
            if is_subdir(lddtree['libs'][lib]['realpath'], wheel_path):
                # we didn't filter libs that resolved via RPATH out
                # earlier because we wanted to make sure to pick up
                # our elf's indirect dependencies. But now we want to
                # filter these ones out, since they're not "external".
                log.debug('RPATH FTW: %s', lib)
                continue
            pol_ext_deps[lib] = lddtree['libs'][lib]['realpath']
        ret[p['name']] = {'libs': pol_ext_deps, 'priority': p['priority']}
    return ret
