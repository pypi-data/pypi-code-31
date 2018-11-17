# coding: utf8
from __future__ import unicode_literals

import pytest
import numpy.random
from thinc.neural.optimizers import Adam
from thinc.neural.ops import NumpyOps
from spacy.attrs import NORM
from spacy.gold import GoldParse
from spacy.vocab import Vocab
from spacy.tokens import Doc
from spacy.pipeline import DependencyParser


@pytest.fixture
def vocab():
    return Vocab(lex_attr_getters={NORM: lambda s: s})


@pytest.fixture
def parser(vocab):
    parser = DependencyParser(vocab)
    parser.cfg['token_vector_width'] = 8
    parser.cfg['hidden_width'] = 30
    parser.cfg['hist_size'] = 0
    parser.add_label('left')
    parser.begin_training([], **parser.cfg)
    sgd = Adam(NumpyOps(), 0.001)

    for i in range(10):
        losses = {}
        doc = Doc(vocab, words=['a', 'b', 'c', 'd'])
        gold = GoldParse(doc, heads=[1, 1, 3, 3],
                deps=['left', 'ROOT', 'left', 'ROOT'])
        parser.update([doc], [gold], sgd=sgd, losses=losses)
    return parser


def test_init_parser(parser):
    pass


# TODO: This is flakey, because it depends on what the parser first learns.
# TODO: This now seems to be implicated in segfaults. Not sure what's up!
@pytest.mark.skip
def test_add_label(parser):
    doc = Doc(parser.vocab, words=['a', 'b', 'c', 'd'])
    doc = parser(doc)
    assert doc[0].head.i == 1
    assert doc[0].dep_ == 'left'
    assert doc[1].head.i == 1
    assert doc[2].head.i == 3
    assert doc[2].head.i == 3
    parser.add_label('right')
    doc = Doc(parser.vocab, words=['a', 'b', 'c', 'd'])
    doc = parser(doc)
    assert doc[0].head.i == 1
    assert doc[0].dep_ == 'left'
    assert doc[1].head.i == 1
    assert doc[2].head.i == 3
    assert doc[2].head.i == 3
    sgd = Adam(NumpyOps(), 0.001)
    for i in range(10):
        losses = {}
        doc = Doc(parser.vocab, words=['a', 'b', 'c', 'd'])
        gold = GoldParse(doc, heads=[1, 1, 3, 3],
                deps=['right', 'ROOT', 'left', 'ROOT'])
        parser.update([doc], [gold], sgd=sgd, losses=losses)
    doc = Doc(parser.vocab, words=['a', 'b', 'c', 'd'])
    doc = parser(doc)
    assert doc[0].dep_ == 'right'
    assert doc[2].dep_ == 'left'
