"""
===========================================================

OGS Smart Money AI

Imbalance Analyzer Tests

===========================================================
"""

from ogs.smart_money.imbalance import (
    ImbalanceAnalyzer,
    ImbalanceDirection,
)

from tests.factories import (
    make_bullish_imbalance_candles,
    make_bearish_imbalance_candles,
    make_candle,
)


def test_empty():

    analyzer = ImbalanceAnalyzer()

    result = analyzer.analyze([])

    assert result.is_empty


def test_less_than_three():

    analyzer = ImbalanceAnalyzer()

    result = analyzer.analyze(
        [
            make_candle(),
            make_candle(),
        ]
    )

    assert result.is_empty


def test_no_imbalance():

    analyzer = ImbalanceAnalyzer()

    result = analyzer.analyze(
        [
            make_candle(),
            make_candle(),
            make_candle(),
        ]
    )

    assert result.is_empty


def test_bullish():

    analyzer = ImbalanceAnalyzer()

    result = analyzer.analyze(
        make_bullish_imbalance_candles()
    )

    assert len(result) == 1

    assert (
        result.first.direction
        == ImbalanceDirection.BULLISH
    )


def test_bearish():

    analyzer = ImbalanceAnalyzer()

    result = analyzer.analyze(
        make_bearish_imbalance_candles()
    )

    assert len(result) == 1

    assert (
        result.first.direction
        == ImbalanceDirection.BEARISH
    )