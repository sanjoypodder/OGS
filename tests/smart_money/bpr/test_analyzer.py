"""
===========================================================

OGS Smart Money AI

Balanced Price Range Analyzer Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRangeAnalyzer,
    BalancedPriceRangeDirection,
)

from ogs.smart_money.fair_value_gap import (
    FairValueGapSeries,
)

from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)


def test_empty_series():

    analyzer = BalancedPriceRangeAnalyzer()

    result = analyzer.analyze(FairValueGapSeries())

    assert len(result) == 0


def test_single_gap():

    analyzer = BalancedPriceRangeAnalyzer()

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())

    result = analyzer.analyze(series)

    assert len(result) == 0


def test_one_bull_one_bear():

    analyzer = BalancedPriceRangeAnalyzer()

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())
    series.append(make_bearish_fair_value_gap())

    result = analyzer.analyze(series)

    assert len(result) == 1


def test_returns_series():

    analyzer = BalancedPriceRangeAnalyzer()

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())
    series.append(make_bearish_fair_value_gap())

    result = analyzer.analyze(series)

    assert result.__class__.__name__ == "BalancedPriceRangeSeries"


def test_direction():

    analyzer = BalancedPriceRangeAnalyzer()

    series = FairValueGapSeries()

    bull = make_bullish_fair_value_gap()
    bear = make_bearish_fair_value_gap()

    series.append(bull)
    series.append(bear)

    result = analyzer.analyze(series)

    assert result.first.direction in (
        BalancedPriceRangeDirection.BULLISH,
        BalancedPriceRangeDirection.BEARISH,
    )


def test_overlap_values():

    analyzer = BalancedPriceRangeAnalyzer()

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())
    series.append(make_bearish_fair_value_gap())

    result = analyzer.analyze(series)

    bpr = result.first

    assert bpr.top > bpr.bottom
    assert bpr.size > 0
    assert bpr.midpoint == (bpr.top + bpr.bottom) / 2


def test_multiple_pairs():

    analyzer = BalancedPriceRangeAnalyzer()

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())
    series.append(make_bullish_fair_value_gap())

    series.append(make_bearish_fair_value_gap())
    series.append(make_bearish_fair_value_gap())

    result = analyzer.analyze(series)

    assert len(result) >= 1