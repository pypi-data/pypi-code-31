# -*- coding: utf-8 -*-

# import...
# ...from HydPy
from hydpy.core import sequencetools


class QA(sequencetools.AideSequence):
    """Seeausfluss (outflow from the lake) [m³/s]."""
    NDIM, NUMERIC = 0, False


class VQ(sequencetools.AideSequence):
    """Hilfsterm (auxiliary term) [m³]."""
    NDIM, NUMERIC = 0, False


class V(sequencetools.AideSequence):
    """Wasservolumen (water volume) [m³]."""
    NDIM, NUMERIC = 0, False


class AideSequences(sequencetools.AideSequences):
    """Aide sequences of HydPy-L-Lake."""
    CLASSES = (QA,
               VQ,
               V)
