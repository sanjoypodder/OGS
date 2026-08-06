import pytest

from ogs.smart_money.liquidity_void import (
    LiquidityVoidValidator,
)
from tests.factories.liquidity_void_factory import (
    make_bullish_liquidity_void,
)


def test_valid():
    lv = make_bullish_liquidity_void()

    LiquidityVoidValidator.validate(lv)


def test_invalid_size():
    lv = make_bullish_liquidity_void()

    object.__setattr__(lv, "size", -1)

    with pytest.raises(ValueError):
        LiquidityVoidValidator.validate(lv)