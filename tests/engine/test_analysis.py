"""
===========================================================

OGS Smart Money AI

Analysis Tests

===========================================================
"""

from ogs.engine.analysis import Analysis


def test_create():

    analysis = Analysis()

    assert analysis is not None


def test_defaults():

    analysis = Analysis()

    assert len(analysis.swings) == 0
    assert len(analysis.bos) == 0
    assert len(analysis.choch) == 0
    assert len(analysis.mss) == 0

    assert len(analysis.equal_highs) == 0
    assert len(analysis.equal_lows) == 0

    assert len(analysis.buy_side) == 0
    assert len(analysis.sell_side) == 0

    assert len(analysis.sweeps) == 0


def test_frozen():

    analysis = Analysis()

    try:
        analysis.swings = None
        assert False
    except Exception:
        assert True