from ogs.smart_money.mitigation import (
    MitigationBlockAnalyzer,
)

from tests.factories.candle_factory import (
    make_candle,
)

from tests.factories.mitigation_factory import (
    make_bearish_mitigation_candles,
    make_bullish_mitigation_candles,
)


def test_empty():
    analyzer = MitigationBlockAnalyzer()

    assert len(
        analyzer.analyze([])
    ) == 0


def test_less_than_two():
    analyzer = MitigationBlockAnalyzer()

    assert len(
        analyzer.analyze(
            [make_candle()]
        )
    ) == 0


def test_bullish():
    analyzer = MitigationBlockAnalyzer()

    result = analyzer.analyze(
        make_bullish_mitigation_candles()
    )

    assert len(result) == 1
    assert result[0].is_bullish


def test_bearish():
    analyzer = MitigationBlockAnalyzer()

    result = analyzer.analyze(
        make_bearish_mitigation_candles()
    )

    assert len(result) == 1
    assert result[0].is_bearish


def test_no_mitigation():
    analyzer = MitigationBlockAnalyzer()

    candles = [
        make_candle(),
        make_candle(),
    ]

    assert len(
        analyzer.analyze(candles)
    ) == 0