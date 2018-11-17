#!/usr/bin/env python3
'''
KLL Compiler
Keyboard Layout Langauge
'''

# Copyright (C) 2014-2018 by Jacob Alexander
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

### Paths ###

import os
import sys
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, path)



### Imports ###

import kll



### Main Entry Point ###


if __name__ == '__main__':
    # See __init__.py
    kll.main(sys.argv[1:])

