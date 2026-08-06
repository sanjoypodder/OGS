"""
Tests for Timeframe statistics.
"""

from ogs.market_data.timeframe import (
    TimeframeCollection,
    TimeframeFactory,
    TimeframeStatistics,
    TimeframeType,
)


def build_collection():

    collection = TimeframeCollection()

    collection.append(TimeframeFactory.create(TimeframeType.M15))
    collection.append(TimeframeFactory.create(TimeframeType.H1))
    collection.append(TimeframeFactory.create(TimeframeType.D1))
    collection.append(TimeframeFactory.create(TimeframeType.W1))

    return collection


def test_count():

    stats = TimeframeStatistics(
        build_collection(),
    )

    assert stats.count == 4


def test_intraday_count():

    stats = TimeframeStatistics(
        build_collection(),
    )

    assert stats.intraday_count == 2


def test_higher_timeframe_count():

    stats = TimeframeStatistics(
        build_collection(),
    )

    assert stats.higher_timeframe_count == 2


def test_shortest():

    stats = TimeframeStatistics(
        build_collection(),
    )

    assert stats.shortest.value is TimeframeType.M15


def test_longest():

    stats = TimeframeStatistics(
        build_collection(),
    )

    assert stats.longest.value is TimeframeType.W1


def test_average_minutes():

    stats = TimeframeStatistics(
        build_collection(),
    )

    expected = (
        15 +
        60 +
        1440 +
        10080
    ) / 4

    assert stats.average_minutes == expected