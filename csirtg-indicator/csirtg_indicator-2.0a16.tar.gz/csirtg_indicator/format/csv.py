import csv
from csirtg_indicator.constants import PYVERSION
from csirtg_indicator import Indicator
from csirtg_indicator.constants import COLUMNS

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

if PYVERSION > 2:
    basestring = (str, bytes)


def get_lines(data, cols=COLUMNS, quoting=csv.QUOTE_ALL):
    output = StringIO()
    csvWriter = csv.DictWriter(output, cols, quoting=quoting)
    csvWriter.writeheader()

    if not isinstance(data, list):
        data = [data]

    for i in data:
        if isinstance(i, Indicator):
            i = i.__dict__()

        r = dict()
        for c in cols:
            y = i.get(c, u'')

            if type(y) is list:
                y = u','.join(y)

            if c == 'confidence' and y is None:
                y = 0.0

            if PYVERSION < 3:
                r[c] = y
                if isinstance(r[c], basestring):
                    r[c] = unicode(r[c]).replace('\n', r'\\n')
                    r[c] = r[c].encode('utf-8', 'ignore')
            else:
                r[c] = y
                if isinstance(r[c], basestring):
                    r[c] = r[c].replace('\n', r'\\n')

        csvWriter.writerow(r)
        yield output.getvalue().rstrip('\r\n')

        if isinstance(output, StringIO):
            output.truncate(0)