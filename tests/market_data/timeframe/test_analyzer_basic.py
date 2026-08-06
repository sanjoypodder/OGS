"""
Tests for TimeframeAnalyzer basic functionality.
"""

from ogs.market_data.timeframe import (
    TimeframeAnalyzer,
    TimeframeCollection,
    TimeframeFactory,
    TimeframeType,
)


def build_collection():

    collection = TimeframeCollection()

    collection.append(TimeframeFactory.create(TimeframeType.M15))
    collection.append(TimeframeFactory.create(TimeframeType.H1))
    collection.append(TimeframeFactory.create(TimeframeType.D1))
    collection.append(TimeframeFactory.create(TimeframeType.W1))

    return collection


def test_intraday():

    analyzer = TimeframeAnalyzer()

    result = analyzer.intraday(build_collection())

    assert len(result) == 2


def test_higher():

    analyzer = TimeframeAnalyzer()

    result = analyzer.higher(build_collection())

    assert len(result) == 2


def test_average_minutes():

    analyzer = TimeframeAnalyzer()

    result = analyzer.average_minutes(
        build_collection(),
    )

    expected = (
        15 +
        60 +
        1440 +
        10080
    ) / 4

    assert result == expected