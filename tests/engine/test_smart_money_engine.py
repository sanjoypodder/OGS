"""
===========================================================

OGS Smart Money AI

Smart Money Engine Tests

===========================================================
"""

from ogs.market import CandleSeries

from tests.factories import make_candle

from ogs.engine import SmartMoneyEngine


def test_create():

    engine = SmartMoneyEngine()

    assert engine is not None


def test_empty():

    engine = SmartMoneyEngine()

    analysis = engine.analyze(
        CandleSeries([])
    )

    assert len(analysis.swings) == 0
    assert len(analysis.equal_highs) == 0
    assert len(analysis.sweeps) == 0


def test_pipeline():

    engine = SmartMoneyEngine()

    candles = CandleSeries(
        [
            make_candle(index=i)
            for i in range(20)
        ]
    )

    analysis = engine.analyze(candles)

    assert analysis is not None

    assert analysis.swings is not None
    assert analysis.bos is not None
    assert analysis.choch is not None
    assert analysis.mss is not None

    assert analysis.equal_highs is not None
    assert analysis.equal_lows is not None

    assert analysis.buy_side is not None
    assert analysis.sell_side is not None

    assert analysis.sweeps is not None