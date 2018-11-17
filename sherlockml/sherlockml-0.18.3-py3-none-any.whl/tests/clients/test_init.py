# Copyright 2018 ASI Data Science
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest

import sherlockml.clients
from sherlockml.clients.account import AccountClient


def test_for_resource():
    assert sherlockml.clients.for_resource("account") is AccountClient


def test_for_resource_missing():
    with pytest.raises(ValueError):
        sherlockml.clients.for_resource("missing")
