"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Fixtures

===========================================================
"""

from __future__ import annotations

import pytest

from tests.factories import (
    make_equal_low,
)

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidity,
    SellSideLiquidityType,
)


@pytest.fixture
def sample_sell_side():

    return SellSideLiquidity(
        equal_low=make_equal_low(),
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )