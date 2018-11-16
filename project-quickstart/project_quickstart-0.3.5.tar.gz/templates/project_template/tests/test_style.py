'''test_style - test coding style confirmation
==============================================

This script modified from:
https://github.com/CGATOxford/CGATPipelines/blob/master/tests/test_style.py

Original author Andreas Heger

:Release: $Id$
:Date: |today|
:Tags: Python

Purpose
-------

This script runs pep8 on all scripts

Currently running with pytest at root dir.
This is largely redundant with flake8?

TO DO: prob delete this file and run flake8 only
'''
import pep8
import glob
import os
from nose.tools import ok_

# DIRECTORIES to examine for python modules/scripts
EXPRESSIONS = (('tests', 'tests/*.py'),
               ('project_quickstart', 'project_quickstart/*.py'),
               )

# Codes to ignore in the pep8 BaseReport
IGNORE = set(('E101',  # indentation contains mixed spaces and tabs
              'E116',  # unexpected indentation (comment)
              'E201',  # whitespace after '('
              'E202',  # whitespace before ')'
              'E122',  # continuation line missing indentation or outdented
              'E251',  # asks for no spaces around =, /, etc.
              'E265',  # block comment should start with '# '
              'E501',  # line too long (82 > 79 characters)
              'E502',  # the backslash is redundant between brackets
              'E731',  # do not assign a lambda expression, use a def
              'W191',
              'W291',
              'W293',
              'W391',
              'W503',  # line break before binary operator
              'W601',
              'W602',
              'files',
              'directories',
              'physical lines',
              'logical lines',))


def check_style(filename):
    '''check style of filename.
    '''

    p = pep8.StyleGuide(quiet=True)
    report = p.check_files([filename])

    # count errors/warning excluding
    # those to ignore
    take = [y for x, y
            in list(report.counters.items()) if x not in IGNORE]
    found = ['%s:%i' % (x, y) for x, y
             in list(report.counters.items()) if x not in IGNORE]
    total = sum(take)
    ok_(total == 0,
        'pep8 style violations: %s' % ','.join(found))


def test_style():
    '''test style of scripts
    '''

    for label, expression in EXPRESSIONS:

        files = glob.glob(expression)
        files.sort()

        for f in files:
            if os.path.isdir(f):
                continue
            check_style.description = os.path.abspath(f)
            yield(check_style, os.path.abspath(f))
