from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)

from ogs.smart_money.fair_value_gap import (
    FairValueGapSeries,
    FairValueGapStatistics,
)


def test_statistics():

    series = FairValueGapSeries()

    series.append(make_bullish_fair_value_gap())
    series.append(make_bearish_fair_value_gap())

    stats = FairValueGapStatistics(series)

    assert stats.total == 2
    assert stats.bullish == 1
    assert stats.bearish == 1
    assert stats.unfilled == 2
    assert stats.filled == 0