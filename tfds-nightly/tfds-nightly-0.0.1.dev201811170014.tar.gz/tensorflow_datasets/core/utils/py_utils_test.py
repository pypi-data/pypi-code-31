# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for py_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils


class PyUtilsTest(tf.test.TestCase):

  def test_map_nested(self):
    """Test the mapping function."""
    def map_fn(x):
      return x * 10

    result = py_utils.map_nested(map_fn, {
        'a': 1,
        'b': {
            'c': 2,
            'e': [3, 4, 5],
        },
    })
    self.assertEqual(result, {
        'a': 10,
        'b': {
            'c': 20,
            'e': [30, 40, 50],
        },
    })

    result = py_utils.map_nested(map_fn, [1, 2, 3])
    self.assertEqual(result, [10, 20, 30])

    result = py_utils.map_nested(map_fn, 1)
    self.assertEqual(result, 10)

  def test_zip_nested(self):
    """Test the zip nested function."""

    arg0 = {
        'a': 1,
        'b': {
            'c': 2,
            'e': [3, 4, 5],
        },
    }
    arg1 = {
        'a': 10,
        'b': {
            'c': 20,
            'e': [30, 40, 50],
        },
    }

    result = py_utils.zip_nested(arg0, arg1)
    self.assertEqual(result, {
        'a': (1, 10),
        'b': {
            'c': (2, 20),
            'e': [(3, 30), (4, 40), (5, 50)],
        },
    })


if __name__ == '__main__':
  tf.test.main()
