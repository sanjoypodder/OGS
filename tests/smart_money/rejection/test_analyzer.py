from ogs.smart_money.rejection import (
    RejectionBlockAnalyzer,
)

from tests.factories.candle_factory import (
    make_candle,
)

from tests.factories.rejection_factory import (
    make_bearish_rejection_candles,
    make_bullish_rejection_candles,
)


def test_empty():
    analyzer = RejectionBlockAnalyzer()

    assert len(
        analyzer.analyze([])
    ) == 0


def test_less_than_two():
    analyzer = RejectionBlockAnalyzer()

    assert len(
        analyzer.analyze(
            [make_candle()]
        )
    ) == 0


def test_bullish():
    analyzer = RejectionBlockAnalyzer()

    result = analyzer.analyze(
        make_bullish_rejection_candles()
    )

    assert len(result) == 1
    assert result[0].is_bullish


def test_bearish():
    analyzer = RejectionBlockAnalyzer()

    result = analyzer.analyze(
        make_bearish_rejection_candles()
    )

    assert len(result) == 1
    assert result[0].is_bearish


def test_no_rejection():
    analyzer = RejectionBlockAnalyzer()

    candles = [
        make_candle(),
        make_candle(),
    ]

    assert len(
        analyzer.analyze(candles)
    ) == 0