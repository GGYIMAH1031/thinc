from __future__ import division

import pytest

from thinc.learner import LinearModel


def test_basic():
    model = LinearModel()
    model.update({1: {1: 1, 3: -5}, 2: {2: 4, 3: 5}}.items())
    #scores = model([1, 2, 3])
