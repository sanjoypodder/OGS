from ogs.smart_money.liquidity_void import (
    LiquidityVoidSeries,
    LiquidityVoidStatistics,
)

from tests.factories.liquidity_void_factory import (
    make_bullish_liquidity_void,
    make_bearish_liquidity_void,
)


def test_statistics():
    series = LiquidityVoidSeries()

    series.append(make_bullish_liquidity_void())
    series.append(make_bearish_liquidity_void())

    stats = LiquidityVoidStatistics(series)

    assert stats.total == 2
    assert stats.bullish == 1
    assert stats.bearish == 1
    assert stats.filled == 0
    assert stats.unfilled == 2