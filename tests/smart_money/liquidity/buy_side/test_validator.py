"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidity,
    BuySideLiquidityType,
    BuySideLiquidityValidator,
)


def test_valid(sample_buy_side):

    validator = BuySideLiquidityValidator()

    validator.validate(sample_buy_side)


def test_none():

    validator = BuySideLiquidityValidator()

    with pytest.raises(ValueError):

        validator.validate(None)


def test_none_equal_high():

    validator = BuySideLiquidityValidator()

    pool = BuySideLiquidity(
        equal_high=None,
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    with pytest.raises(ValueError):

        validator.validate(pool)