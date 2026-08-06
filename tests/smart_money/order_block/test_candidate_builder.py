"""
===========================================================

OGS Smart Money AI

Order Block Candidate Builder Tests

===========================================================
"""

from ogs.smart_money.candidate import CandidateStatus

from ogs.smart_money.order_block.candidate_builder import (
    OrderBlockCandidateBuilder,
)

from tests.factories import (
    make_bearish_candle,
    make_bullish_mss,
    make_buy_side_liquidity,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    SweepDirection,
    SweepStatus,
)


def test_build_candidate():

    builder = OrderBlockCandidateBuilder()

    candle = make_bearish_candle()

    mss = make_bullish_mss()

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=candle,
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    candidate = builder.build(
        origin_candle=candle,
        mss=mss,
        liquidity_sweep=sweep,
    )

    assert candidate.origin_candle == candle
    assert candidate.mss == mss
    assert candidate.liquidity_sweep == sweep
    assert candidate.status == CandidateStatus.DETECTED


def test_candidate_timestamp():

    builder = OrderBlockCandidateBuilder()

    candle = make_bearish_candle()

    mss = make_bullish_mss()

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=candle,
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    candidate = builder.build(
        origin_candle=candle,
        mss=mss,
        liquidity_sweep=sweep,
    )

    assert candidate.timestamp == candle.timestamp
    