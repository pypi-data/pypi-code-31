#
# Copyright (c) 2011, 2015
#  Adam Tauno Williams <awilliam@whitemice.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE
#
from coils.foundation import Team, apply_orm_hints_to_query
from coils.core.logic import SearchCommand
from keymap import COILS_TEAM_KEYMAP


class SearchTeams(SearchCommand):
    __domain__ = "team"
    __operation__ = "search"
    mode = None

    def __init__(self):
        SearchCommand.__init__(self)

    def prepare(self, ctx, **params):
        SearchCommand.prepare(self, ctx, **params)

    def parse_parameters(self, **params):
        SearchCommand.parse_parameters(self, **params)

    def add_result(self, team):
        if (team not in self._result):
            self._result.append(team)

    @property
    def search_keymap(self):
        keymap = COILS_TEAM_KEYMAP.copy()
        return keymap

    def _custom_search_criteria(self, key, value, conjunction, expression, ):
        # unsupported custom key
        return (None, None, None, None, None, )

    def run(self):
        self._query = self._parse_criteria(
            self._criteria, Team, self.search_keymap,
        )
        self._query = apply_orm_hints_to_query(
            self._query, Team, self.orm_hints,
        )
        data = self._query.all()
        self.log.debug('team search returned {0} objects'.format(len(data), ))
        self.set_return_value(data)
        return
