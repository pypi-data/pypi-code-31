# -*- coding: utf-8 -*-
"""Format adapter for sql."""

from cli_helpers.utils import filter_dict_by_key
from athenacli.packages.parseutils import extract_tables

supported_formats = ('sql-insert', 'sql-update', 'sql-update-1',
                     'sql-update-2', )

preprocessors = ()


def adapter(data, headers, table_format=None, **kwargs):
    tables = extract_tables(formatter.query)
    if len(tables) > 0:
        table = tables[0]
        if table[0]:
            table_name = "{}.{}".format(*table[:2])
        else:
            table_name = table[1]
    else:
        table_name = "`DUAL`"
    escape = formatter.mycli.sqlexecute.conn.escape
    if table_format == 'sql-insert':
        h = "`, `".join(headers)
        yield "INSERT INTO {} (`{}`) VALUES".format(table_name, h)
        prefix = "  "
        for d in data:
            values = ", ".join(escape(v) for i, v in enumerate(d))
            yield "{}({})".format(prefix, values)
            if prefix == "  ":
                prefix = ", "
        yield ";"
    if table_format.startswith('sql-update'):
        s = table_format.split('-')
        keys = 1
        if len(s) > 2:
            keys = int(s[-1])
        for d in data:
            yield "UPDATE {} SET".format(table_name)
            prefix = "  "
            for i, v in enumerate(d[keys:], keys):
                yield "{}`{}` = {}".format(prefix, headers[i], escape(v))
                if prefix == "  ":
                    prefix = ", "
            f = "`{}` = {}"
            where = (f.format(headers[i], escape(d[i])) for i in range(keys))
            yield "WHERE {};".format(" AND ".join(where))


def register_new_formatter(TabularOutputFormatter):
    global formatter
    formatter = TabularOutputFormatter
    for sql_format in supported_formats:
        TabularOutputFormatter.register_new_formatter(
            sql_format, adapter, preprocessors, {'table_format': sql_format})