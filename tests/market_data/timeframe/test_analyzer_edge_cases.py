"""
Tests for TimeframeAnalyzer edge cases.
"""

from ogs.market_data.timeframe import (
    TimeframeAnalyzer,
    TimeframeCollection,
    TimeframeFactory,
    TimeframeType,
)


def test_empty_collection():

    analyzer = TimeframeAnalyzer()

    collection = TimeframeCollection()

    assert analyzer.shortest(collection) is None
    assert analyzer.longest(collection) is None
    assert analyzer.average_minutes(collection) == 0.0

    result = analyzer.analyze(collection)

    assert result["count"] == 0
    assert result["intraday"] == 0
    assert result["higher"] == 0
    assert result["shortest"] is None
    assert result["longest"] is None


def test_single_timeframe():

    analyzer = TimeframeAnalyzer()

    collection = TimeframeCollection()

    timeframe = TimeframeFactory.create(
        TimeframeType.H1,
    )

    collection.append(timeframe)

    assert analyzer.shortest(collection) == timeframe
    assert analyzer.longest(collection) == timeframe


def test_only_intraday():

    analyzer = TimeframeAnalyzer()

    collection = TimeframeCollection()

    collection.append(TimeframeFactory.create(TimeframeType.M1))
    collection.append(TimeframeFactory.create(TimeframeType.M15))
    collection.append(TimeframeFactory.create(TimeframeType.H4))

    result = analyzer.analyze(collection)

    assert result["count"] == 3
    assert result["intraday"] == 3
    assert result["higher"] == 0


def test_only_higher():

    analyzer = TimeframeAnalyzer()

    collection = TimeframeCollection()

    collection.append(TimeframeFactory.create(TimeframeType.D1))
    collection.append(TimeframeFactory.create(TimeframeType.W1))
    collection.append(TimeframeFactory.create(TimeframeType.MN1))

    result = analyzer.analyze(collection)

    assert result["count"] == 3
    assert result["intraday"] == 0
    assert result["higher"] == 3