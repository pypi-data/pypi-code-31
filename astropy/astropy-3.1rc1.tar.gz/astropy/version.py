# Autogenerated by Astropy's setup.py on 2018-11-16 00:56:02 UTC
from __future__ import unicode_literals
import datetime

version = "3.1rc1"
githash = "3db76a460c8ee55f68100bed880887526cc13dd9"


major = 3
minor = 1
bugfix = 0

version_info = (major, minor, bugfix)

release = True
timestamp = datetime.datetime(2018, 11, 16, 0, 56, 2)
debug = False

astropy_helpers_version = "3.1rc1"

try:
    from ._compiler import compiler
except ImportError:
    compiler = "unknown"

try:
    from .cython_version import cython_version
except ImportError:
    cython_version = "unknown"
