"""
===========================================================

OGS Smart Money AI

Displacement Analyzer Tests

===========================================================
"""

from ogs.smart_money.order_block.displacement import (
    DisplacementAnalyzer,
    DisplacementDirection,
)

from tests.factories import (
    make_bearish_candle,
    make_bullish_candle,
    make_candle,
)


def test_empty():

    analyzer = DisplacementAnalyzer()

    result = analyzer.analyze([])

    assert result.is_empty


def test_bullish():

    analyzer = DisplacementAnalyzer()

    result = analyzer.analyze(
        [
            make_bullish_candle(),
        ]
    )

    assert len(result) == 1
    assert result.first.direction == (
        DisplacementDirection.BULLISH
    )


def test_bearish():

    analyzer = DisplacementAnalyzer()

    result = analyzer.analyze(
        [
            make_bearish_candle(),
        ]
    )

    assert len(result) == 1
    assert result.first.direction == (
        DisplacementDirection.BEARISH
    )


def test_neutral():

    analyzer = DisplacementAnalyzer()

    result = analyzer.analyze(
        [
            make_candle(),
        ]
    )

    assert result.is_empty


def test_multiple():

    analyzer = DisplacementAnalyzer()

    result = analyzer.analyze(
        [
            make_bullish_candle(),
            make_bearish_candle(),
            make_candle(),
        ]
    )

    assert len(result) == 2

    assert (
        result[0].direction
        == DisplacementDirection.BULLISH
    )

    assert (
        result[1].direction
        == DisplacementDirection.BEARISH
    )