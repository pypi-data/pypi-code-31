#
# Copyright (c) 2010, 2015
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
from coils.core import AuthenticationToken, Command, CoilsException
from coils.core.logic import DeleteCommand
from command import TokenCommand


class DeleteToken(Command, TokenCommand):
    __domain__ = "token"
    __operation__ = "delete"

    def prepare(self, ctx, **params):
        Command.prepare(self, ctx, **params)

    def parse_parameters(self, **params):
        Command.parse_parameters(self, **params)
        self._token = params.get('token', None)
        if (self._token is None):
            raise CoilsException('No token provided for deletion')

    def run(self):
        db = self._ctx.db_session()
        if (isinstance(self._token, basestring)):
            query = db.query(AuthenticationToken).filter(
                AuthenticationToken.token == self._token
            )
            self._token = query.first()
        """
        NOTE: If token is not a string, we assume it is an
        AuthenticationToken entity
        """
        if (self._token is not None):
            self._ctx.db_session().delete(self._token)
            self._result = True
        else:
            self._result = False
