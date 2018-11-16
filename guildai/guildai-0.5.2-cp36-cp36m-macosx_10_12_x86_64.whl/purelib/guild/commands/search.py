# Copyright 2017-2018 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

import click

from guild import click_util

@click.command()
@click.argument("terms", metavar="TERM...", nargs=-1, required=True)
@click.option(
    "-a", "--all",
    is_flag=True,
    help="Search all packages.")

@click_util.use_args

def search(args):
    """Search for a package.

    Specify one or more `TERM` arguments to search for.

    By default, only Guild packages are returned. To search all Python
    packages, use the `--all` option.

    """
    from . import search_impl
    search_impl.main(args)
