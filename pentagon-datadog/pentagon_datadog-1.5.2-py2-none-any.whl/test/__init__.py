
# Copyright 2018 ReactiveOps

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import hashlib
import os
import logging

from pentagon_datadog.dashboard import Dashboard
from pentagon_datadog.monitor import Monitor
import oyaml as yaml


class TestDashboards(unittest.TestCase):
    name = "test-dashboards"
    test_input_file = "test/files/test_input.yml"

    def setUp(self):
        with open(self.test_input_file) as f:
            self._data = yaml.load(f.read())

        for dash in self._data.get('dashboards'):
            d = Dashboard(dash)
            d.add("./", overwrite=True)

    def test_dashboard_output(self):
        gold = hashlib.md5(open("test/files/reactiveops_kubernetes_resource_timeboard.tf").read()).hexdigest()
        new =hashlib.md5(open("reactiveops_kubernetes_resource_timeboard.tf").read()).hexdigest()

        logging.debug(gold)
        logging.debug(new)

        self.assertEqual(gold, new)

    def tearDown(self):
        os.remove("reactiveops_kubernetes_resource_timeboard.tf")


class TestMonitors(unittest.TestCase):
    name = "test-monitors"
    test_input_file = "test/files/test_input.yml"

    def setUp(self):
        with open(self.test_input_file) as f:
            self._data = yaml.load(f.read())
        global_definitions = self._data.get('definitions',{})
        for monitor in self._data.get('monitors'):
            m = Monitor(monitor)
            m._global_definitions = global_definitions
            m.add('./', overwrite=True)

    def test_monitor_output(self):
        gold = hashlib.md5(open("test/files/test_increase_in_network_bytes_received.tf").read()).hexdigest()
        new =hashlib.md5(open("test_increase_in_network_bytes_received.tf").read()).hexdigest()

        logging.debug(gold)
        logging.debug(new)

        self.assertEqual(gold, new)

    def tearDown(self):
        os.remove("test_increase_in_network_bytes_received.tf")
