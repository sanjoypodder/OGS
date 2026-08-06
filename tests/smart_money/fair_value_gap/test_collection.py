from tests.factories import (
    make_bullish_fair_value_gap,
)

from ogs.smart_money.fair_value_gap import (
    FairValueGapSeries,
)


def test_append():

    series = FairValueGapSeries()

    gap = make_bullish_fair_value_gap()

    series.append(gap)

    assert len(series) == 1
    assert series.first == gap
    assert series.last == gap


def test_latest():

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())
    series.append(make_bullish_fair_value_gap())

    assert len(series.latest()) == 1
    assert len(series.latest(2)) == 2