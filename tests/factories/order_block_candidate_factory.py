"""
===========================================================

OGS Smart Money AI

Order Block Candidate Factory

===========================================================
"""

from ogs.smart_money.candidate import CandidateStatus

from ogs.smart_money.order_block import (
    OrderBlockCandidate,
)

from .candle_factory import make_bearish_candle
from .mss_factory import make_bullish_mss
from .buy_side_factory import make_buy_side_liquidity
from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    SweepDirection,
    SweepStatus,
)


def make_bullish_order_block_candidate():

    candle = make_bearish_candle(index=2)

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=candle,
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    return OrderBlockCandidate(
        status=CandidateStatus.DETECTED,
        origin_candle=candle,
        mss=make_bullish_mss(index=10),
        liquidity_sweep=sweep,
    )