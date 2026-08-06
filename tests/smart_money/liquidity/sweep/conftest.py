"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Fixtures

===========================================================
"""

from __future__ import annotations

import pytest

from tests.factories import (
    make_buy_side_liquidity,
    make_candle,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    SweepDirection,
    SweepStatus,
)


@pytest.fixture
def sample_sweep():

    return LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=make_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )