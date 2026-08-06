"""
===========================================================

OGS Smart Money AI

Order Block Candidate Generation Tests

===========================================================
"""

from ogs.engine import Analysis
from ogs.market import CandleSeries

from ogs.smart_money.order_block import (
    OrderBlockAnalyzer,
)

from tests.factories import (
    make_bearish_candle,
    make_bullish_candle,
    make_bullish_mss,
    make_buy_side_liquidity,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    LiquiditySweepSeries,
    SweepDirection,
    SweepStatus,
)

from ogs.smart_money.mss import MSSSeries


def make_sweep():

    candle = make_bearish_candle(index=2)

    return LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=candle,
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )


def test_no_sweeps():

    analyzer = OrderBlockAnalyzer()

    analysis = Analysis(
        sweeps=LiquiditySweepSeries([]),
        mss=MSSSeries([]),
    )

    assert (
        analyzer.candidate_count(
            CandleSeries([]),
            analysis,
        )
        == 0
    )


def test_no_mss():

    analyzer = OrderBlockAnalyzer()

    analysis = Analysis(
        sweeps=LiquiditySweepSeries(
            [
                make_sweep(),
            ]
        ),
        mss=MSSSeries([]),
    )

    assert (
        analyzer.candidate_count(
            CandleSeries([]),
            analysis,
        )
        == 0
    )


def test_single_candidate():

    analyzer = OrderBlockAnalyzer()

    candles = CandleSeries(
        [
            make_bullish_candle(index=1),
            make_bearish_candle(index=2),
            make_bullish_candle(index=3),
            make_bullish_candle(index=4),
            make_bullish_candle(index=5),
            make_bullish_candle(index=6),
            make_bullish_candle(index=7),
            make_bullish_candle(index=8),
            make_bullish_candle(index=9),
            make_bullish_candle(index=10),
        ]
    )

    analysis = Analysis(
        sweeps=LiquiditySweepSeries(
            [
                make_sweep(),
            ]
        ),
        mss=MSSSeries(
            [
                make_bullish_mss(index=10),
            ]
        ),
    )

    candidates = analyzer._build_candidates(
        candles,
        analysis,
    )

    assert len(candidates) == 1

    assert (
        candidates[0].origin_candle.timestamp
        == make_bearish_candle(index=2).timestamp
    )