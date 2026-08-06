from ogs.smart_money.liquidity_void import LiquidityVoidSeries
from tests.factories.liquidity_void_factory import (
    make_bullish_liquidity_void,
)


def test_append():
    series = LiquidityVoidSeries()

    series.append(make_bullish_liquidity_void())

    assert len(series) == 1


def test_iteration():
    series = LiquidityVoidSeries()

    series.append(make_bullish_liquidity_void())

    assert list(series)