#
# Copyright (c) 2014
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
# THE SOFTWARE.
#
import pprint
from coils.net import PathObject


class RPC2LogObject(PathObject):

    def __init__(self, parent, name, **params):
        self.name = name
        PathObject.__init__(self, parent, **params)

    def is_public(self):
        return False

    def get_name(self):
        return self.name

    def do_GET(self):
        data = self.context.run_command(
            'admin::get-rpc2-log',
        )

        if 'status' in self.parameters:
            status = self.parameters['status'][0]
            data = [x for x in data if x['status'] == status]

        if 'method' in self.parameters:
            method = self.parameters['method'][0]
            data = [x for x in data if x['method'] == method]

        if 'login' in self.parameters:
            login = self.parameters['login'][0]
            data = [x for x in data if x['login'] == login]

        if 'errors' in self.parameters:
            data = [x for x in data if x['errors'] > 0]

        data = pprint.pformat(data)
        self.request.simple_response(
            200, mimetype='text/plain', data=data,
        )
