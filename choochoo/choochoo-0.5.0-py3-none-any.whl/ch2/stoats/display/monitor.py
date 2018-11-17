
from urwid import Text, Columns, Pile

from . import Displayer
from ..calculate.monitor import MonitorStatistics
from ..names import STEPS, REST_HR, DAILY_STEPS
from ...lib.date import to_date
from ...squeal.tables.statistic import StatisticJournal, StatisticName
from ...uweird.fields import ReadOnlyField
from ...uweird.fields.summary import summary_columns
from ...uweird.tui.decorators import Indent


class MonitorDiary(Displayer):

    def build(self, s, f, date, schedule=None):
        date = to_date(date)
        if schedule:
            yield from self.__build_schedule(s, f, date, schedule)
        else:
            yield from self.__build_date(s, date)

    def __build_date(self, s, date):
        columns = self.__fields(s, date)
        if columns:
            yield Pile([Text('Monitor'),
                        Indent(Columns(columns))])

    def __fields(self, s, date):
        steps = self.__field(s, date, DAILY_STEPS)
        rest_hr = self.__field(s, date, REST_HR)
        if steps or rest_hr:
            return [steps if steps else Text(''), rest_hr if rest_hr else Text('')]
        else:
            return None

    def __field(self, s, date, name):
        sjournal = StatisticJournal.at_date(s, date, name, MonitorStatistics, None)
        if sjournal:
            return ReadOnlyField(self._log, sjournal, date=date).widget()
        else:
            return None

    def __build_schedule(self, s, f, date, schedule):
        columns = list(self.__schedule_fields(s, f, date, schedule))
        if columns:
            yield Pile([Text('Monitor'),
                        Indent(Pile(columns))])

    def __schedule_fields(self, s, f, date, schedule):
        names = list(self.__names(s, STEPS, REST_HR))
        yield from summary_columns(self._log, s, f, date, schedule, names)

    def __names(self, s, *names):
        for name in names:
            yield s.query(StatisticName). \
                filter(StatisticName.name == name,
                       StatisticName.owner == MonitorStatistics).one()
