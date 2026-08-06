"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidity,
    SellSideLiquidityType,
    SellSideLiquidityValidator,
)


def test_valid(sample_sell_side):

    validator = SellSideLiquidityValidator()

    validator.validate(sample_sell_side)


def test_none():

    validator = SellSideLiquidityValidator()

    with pytest.raises(ValueError):

        validator.validate(None)


def test_none_equal_low():

    validator = SellSideLiquidityValidator()

    pool = SellSideLiquidity(
        equal_low=None,
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    with pytest.raises(ValueError):

        validator.validate(pool)