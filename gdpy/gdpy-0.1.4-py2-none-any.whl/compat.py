# -*- coding: utf-8 -*-

"""
compat Python releases
"""

import sys

is_py2 = (sys.version_info[0] == 2)
is_py3 = (sys.version_info[0] == 3)


try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json


if is_py2:
    from urllib import quote as urlquote, unquote as urlunquote
    from urlparse import urlparse

    def to_json(data):
        """dict 2 json"""
        return json.dumps(data)

    def to_bytes(data):
        """unicode to utf-8 bytes；else return directly"""
        if isinstance(data, unicode):
            return data.encode('utf-8')
        else:
            return data

    def to_string(data):
        """2 string"""
        return to_bytes(data)

    def to_unicode(data):
        """2 unicode"""
        if isinstance(data, bytes):
            return data.decode('utf-8')
        else:
            return data

    def stringify(input):
        if isinstance(input, dict):
            return dict([(stringify(key), stringify(value)) for key, value in input.iteritems()])
        elif isinstance(input, list):
            return [stringify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

    builtin_str = str
    bytes = str
    str = unicode


elif is_py3:
    from urllib.parse import quote as urlquote, unquote as urlunquote
    from urllib.parse import urlparse

    def to_json(data):
        """dict 2 json"""
        return json.dumps(data)

    def to_bytes(data):
        """unicode to utf-8 bytes；else return directly"""
        if isinstance(data, str):
            return data.encode(encoding='utf-8')
        else:
            return data

    def to_string(data):
        """unicode to utf-8 bytes；else return directly"""
        if isinstance(data, bytes):
            return data.decode('utf-8')
        else:
            return data

    def to_unicode(data):
        """2 unicode"""
        return to_string(data)

    def stringify(input):
        return input

    builtin_str = str
    bytes = bytes
    str = str
