"""
===========================================================

OGS Smart Money AI

Market Structure Engine Tests

===========================================================
"""

from ogs.market import CandleSeries

from tests.factories import (
    make_candle,
)

from ogs.engine.market_structure_engine import (
    MarketStructureEngine,
)


def test_create():

    engine = MarketStructureEngine()

    assert engine is not None


def test_empty():

    engine = MarketStructureEngine()

    analysis = engine.analyze(
        CandleSeries([])
    )

    assert len(analysis.swings) == 0
    assert len(analysis.bos) == 0
    assert len(analysis.choch) == 0
    assert len(analysis.mss) == 0


def test_pipeline():

    engine = MarketStructureEngine()

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