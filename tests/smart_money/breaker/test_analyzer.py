from ogs.smart_money.breaker import (
    BreakerBlockAnalyzer,
)

from tests.factories.candle_factory import make_candle
from tests.factories.breaker_factory import (
    make_bullish_breaker_candles,
    make_bearish_breaker_candles,
)


def test_empty():
    analyzer = BreakerBlockAnalyzer()

    assert len(analyzer.analyze([])) == 0


def test_less_than_two():
    analyzer = BreakerBlockAnalyzer()

    assert len(analyzer.analyze([make_candle()])) == 0


def test_bullish():
    analyzer = BreakerBlockAnalyzer()

    result = analyzer.analyze(
        make_bullish_breaker_candles()
    )

    assert len(result) == 1
    assert result[0].is_bullish


def test_bearish():
    analyzer = BreakerBlockAnalyzer()

    result = analyzer.analyze(
        make_bearish_breaker_candles()
    )

    assert len(result) == 1
    assert result[0].is_bearish


def test_no_breaker():
    analyzer = BreakerBlockAnalyzer()

    candles = [
        make_candle(),
        make_candle(),
    ]

    assert len(analyzer.analyze(candles)) == 0