
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

import logging

from pentagon_datadog.rodd import Rodd


class Dashboard(Rodd):
    template_file_name = 'dashboard.tf.jinja'
    _item_type = 'dashboards'


class Dashboards(Rodd):

    def add(self, destination, overwrite=False):
        logging.debug("Adding dashboard .tf files")
        global_definitions = self._data.get('definitions', {})
        try:
            for dash in self._data.get('dashboards'):
                logging.debug(dash)
                d = Dashboard(dash)
                d._global_definitions = global_definitions
                d.add(destination, overwrite=True)
        except TypeError, e:
            logging.debug(e)
            logging.error("No dashboards declared or no file argument passed.")
