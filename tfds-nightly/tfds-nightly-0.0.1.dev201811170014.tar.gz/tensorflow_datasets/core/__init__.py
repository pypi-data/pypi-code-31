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

"""tensorflow_datasets.core."""

from tensorflow_datasets.core.dataset_builder import DatasetBuilder
from tensorflow_datasets.core.dataset_builder import GeneratorBasedDatasetBuilder

from tensorflow_datasets.core.dataset_info import DatasetInfo

from tensorflow_datasets.core.splits import NamedSplit
from tensorflow_datasets.core.splits import SplitDict
from tensorflow_datasets.core.splits import SplitGenerator
from tensorflow_datasets.core.splits import SplitInfo

__all__ = [
    "DatasetBuilder",
    "GeneratorBasedDatasetBuilder",
    "DatasetInfo",
    "NamedSplit",
    "SplitDict",
    "SplitGenerator",
    "SplitInfo",
]
