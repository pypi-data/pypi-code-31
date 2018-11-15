#
# Copyright (c) 2010 Adam Tauno Williams <awilliam@whitemice.org>
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
from coils.core                   import *
from coils.core.logic             import MacroCommand

class ModulusMacro(MacroCommand):
    __domain__ = "macro"
    __operation__ = "modulus"

    @property
    def descriptor(self):
        return { 'name': 'modulus',
                 'parameters': { 'var1': {'type': 'numeric'},
                                 'var2': {'type': 'numeric'} },
                 'help': 'modulus returns remainder from given values for division' }

    def parse_parameters(self, **params):
        MacroCommand.parse_parameters(self, **params)
        self._var1 = params.get('var1', None)
        self._var2 = params.get('var2', None)
        if (self._var1 is None) or (self._var2 is None):
            raise CoilsException('NULL input provided to modulus macro')
        if( not isinstance(self._var1,(int,float)) or not isinstance(self._var2,(int,float))):
            raise CoilsException('Non-numeric value provided to modulus macro')

    def run(self):
        self.set_result(self._var1 % self._var2)

