"""
===========================================================

OGS Smart Money AI

Fair Value Gap Analyzer Tests

===========================================================
"""

from ogs.smart_money.fair_value_gap import (
    FairValueGapAnalyzer,
    FairValueGapDirection,
)

from tests.factories import (
    make_bullish_fvg_candles,
    make_bearish_fvg_candles,
    make_candle,
)


def test_empty():

    analyzer = FairValueGapAnalyzer()

    result = analyzer.analyze([])

    assert result.is_empty


def test_less_than_three():

    analyzer = FairValueGapAnalyzer()

    result = analyzer.analyze(
        [
            make_candle(),
            make_candle(),
        ]
    )

    assert result.is_empty


def test_no_gap():

    analyzer = FairValueGapAnalyzer()

    result = analyzer.analyze(
        [
            make_candle(),
            make_candle(),
            make_candle(),
        ]
    )

    assert result.is_empty


def test_bullish():

    analyzer = FairValueGapAnalyzer()

    result = analyzer.analyze(
        make_bullish_fvg_candles()
    )

    assert len(result) == 1

    gap = result.first

    assert gap.direction == FairValueGapDirection.BULLISH
    assert gap.top == 105
    assert gap.bottom == 100
    assert gap.midpoint == 102.5
    assert gap.size == 5


def test_bearish():

    analyzer = FairValueGapAnalyzer()

    result = analyzer.analyze(
        make_bearish_fvg_candles()
    )

    assert len(result) == 1

    gap = result.first

    assert gap.direction == FairValueGapDirection.BEARISH
    assert gap.top == 100
    assert gap.bottom == 95
    assert gap.midpoint == 97.5
    assert gap.size == 5