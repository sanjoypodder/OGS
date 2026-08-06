from ogs.smart_money.liquidity_void import (
    LiquidityVoidAnalyzer,
)

from tests.factories.candle_factory import make_candle
from tests.factories.liquidity_void_factory import (
    make_bullish_liquidity_void_candles,
    make_bearish_liquidity_void_candles,
)


def test_empty():
    analyzer = LiquidityVoidAnalyzer()

    assert len(analyzer.analyze([])) == 0


def test_less_than_three():
    analyzer = LiquidityVoidAnalyzer()

    candles = [
        make_candle(),
        make_candle(),
    ]

    assert len(analyzer.analyze(candles)) == 0


def test_bullish():
    analyzer = LiquidityVoidAnalyzer()

    result = analyzer.analyze(
        make_bullish_liquidity_void_candles()
    )

    assert len(result) == 1
    assert result[0].is_bullish


def test_bearish():
    analyzer = LiquidityVoidAnalyzer()

    result = analyzer.analyze(
        make_bearish_liquidity_void_candles()
    )

    assert len(result) == 1
    assert result[0].is_bearish


def test_no_void():
    analyzer = LiquidityVoidAnalyzer()

    candles = [
        make_candle(),
        make_candle(),
        make_candle(),
    ]

    assert len(analyzer.analyze(candles)) == 0