"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Analyzer Tests

===========================================================
"""

from tests.factories import (
    make_buy_side_liquidity,
    make_candle,
)

from ogs.market import CandleSeries

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquiditySeries,
)

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquiditySeries,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweepAnalyzer,
    SweepDirection,
)
def test_empty():

    analyzer = LiquiditySweepAnalyzer()

    result = analyzer.analyze(
        CandleSeries([]),
        BuySideLiquiditySeries([]),
        SellSideLiquiditySeries([]),
    )

    assert len(result) == 0

def test_no_liquidity():

    analyzer = LiquiditySweepAnalyzer()

    result = analyzer.analyze(
        CandleSeries(
            [
                make_candle(),
            ]
        ),
        BuySideLiquiditySeries([]),
        SellSideLiquiditySeries([]),
    )

    assert len(result) == 0

from dataclasses import replace


def test_buy_side_sweep():

    analyzer = LiquiditySweepAnalyzer()

    candle = replace(
        make_candle(),
        high=make_candle().high.__class__(
            make_candle().symbol,
            111,
        ),
        close=make_candle().close.__class__(
            make_candle().symbol,
            109,
        ),
    )

    result = analyzer.analyze(
        CandleSeries(
            [
                candle,
            ]
        ),
        BuySideLiquiditySeries(
            [
                make_buy_side_liquidity(),
            ]
        ),
        SellSideLiquiditySeries([]),
    )

    assert len(result) == 1

    sweep = result.first

    assert sweep.direction == SweepDirection.BUY_SIDE

def test_order_preserved():

    analyzer = LiquiditySweepAnalyzer()

    candle = replace(
        make_candle(),
        high=make_candle().high.__class__(
            make_candle().symbol,
            111,
        ),
        close=make_candle().close.__class__(
            make_candle().symbol,
            109,
        ),
    )

    result = analyzer.analyze(
        CandleSeries(
            [
                candle,
            ]
        ),
        BuySideLiquiditySeries(
            [
                make_buy_side_liquidity(),
            ]
        ),
        SellSideLiquiditySeries([]),
    )

    assert result.first.liquidity_pool is not None
    