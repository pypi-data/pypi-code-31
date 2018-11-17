
from tempfile import NamedTemporaryFile

from sqlalchemy.sql.functions import count

from ch2.command.activities import activities
from ch2.command.args import bootstrap_file, m, V, DEV, mm, FAST
from ch2.command.constants import constants
from ch2.config.default import default
from ch2.squeal.tables.activity import ActivityJournal
from ch2.squeal.tables.pipeline import PipelineType
from ch2.squeal.tables.statistic import StatisticJournal
from ch2.stoats.calculate import run_pipeline_after


def test_activities():

    with NamedTemporaryFile() as f:

        args, log, db = bootstrap_file(f, m(V), '5')

        bootstrap_file(f, m(V), '5', mm(DEV), configurator=default)

        args, log, db = bootstrap_file(f, m(V), '5', 'constants', '--set', 'FTHR.%', '154')
        constants(args, log, db)

        args, log, db = bootstrap_file(f, m(V), '5', 'constants', 'FTHR.%')
        constants(args, log, db)

        args, log, db = bootstrap_file(f, m(V), '5', mm(DEV),
                                       'activities', mm(FAST), 'data/test/personal/2018-08-27-rec.fit')
        activities(args, log, db)

        # run('sqlite3 %s ".dump"' % f.name, shell=True)

        run_pipeline_after(log, db, PipelineType.STATISTIC, force=True, after='2018-01-01')

        # run('sqlite3 %s ".dump"' % f.name, shell=True)

        with db.session_context() as s:
            n = s.query(count(StatisticJournal.id)).scalar()
            assert n == 10530, n
            journal = s.query(ActivityJournal).one()
            assert journal.start != journal.finish

