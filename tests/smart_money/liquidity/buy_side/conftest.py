"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Fixtures

===========================================================
"""

from __future__ import annotations

from decimal import Decimal

import pytest

from tests.factories import make_swing_high

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighType,
)

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidity,
    BuySideLiquidityType,
)


@pytest.fixture
def sample_buy_side():

    equal_high = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    return BuySideLiquidity(
        equal_high=equal_high,
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )