"""
===========================================================

OGS Smart Money AI

Liquidity Engine Tests

===========================================================
"""

from ogs.market import CandleSeries

from tests.factories import make_candle

from ogs.engine.liquidity_engine import (
    LiquidityEngine,
)

from ogs.smart_money.swing import SwingSeries


def test_create():

    engine = LiquidityEngine()

    assert engine is not None


def test_empty():

    engine = LiquidityEngine()

    analysis = engine.analyze(
        CandleSeries([]),
        SwingSeries([]),
    )

    assert len(analysis.equal_highs) == 0
    assert len(analysis.equal_lows) == 0
    assert len(analysis.buy_side) == 0
    assert len(analysis.sell_side) == 0
    assert len(analysis.sweeps) == 0


def test_pipeline():

    engine = LiquidityEngine()

    candles = CandleSeries(
        [
            make_candle(index=i)
            for i in range(20)
        ]
    )

    swings = SwingSeries([])

    analysis = engine.analyze(
        candles,
        swings,
    )

    assert analysis.equal_highs is not None
    assert analysis.equal_lows is not None
    assert analysis.buy_side is not None
    assert analysis.sell_side is not None
    assert analysis.sweeps is not None