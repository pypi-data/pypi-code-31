# Natural Language Toolkit: Inference
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Dan Garrette <dhgarrette@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
#
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Classes and interfaces for theorem proving and model building.
"""

from nltk.inference.api import ParallelProverBuilder, ParallelProverBuilderCommand
from nltk.inference.mace import Mace, MaceCommand
from nltk.inference.prover9 import Prover9, Prover9Command
from nltk.inference.resolution import ResolutionProver, ResolutionProverCommand
from nltk.inference.tableau import TableauProver, TableauProverCommand
from nltk.inference.discourse import (
    ReadingCommand,
    CfgReadingCommand,
    DrtGlueReadingCommand,
    DiscourseTester,
)
