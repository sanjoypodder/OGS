"""
Tests for TimeframeAnalyzer detection methods.
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
    collection.append(TimeframeFactory.create(TimeframeType.MN1))

    return collection


def test_shortest():

    analyzer = TimeframeAnalyzer()

    timeframe = analyzer.shortest(
        build_collection(),
    )

    assert timeframe.value is TimeframeType.M15


def test_longest():

    analyzer = TimeframeAnalyzer()

    timeframe = analyzer.longest(
        build_collection(),
    )

    assert timeframe.value is TimeframeType.MN1


def test_analyze():

    analyzer = TimeframeAnalyzer()

    result = analyzer.analyze(
        build_collection(),
    )

    assert result["count"] == 5
    assert result["intraday"] == 2
    assert result["higher"] == 3


def test_analyze_returns_objects():

    analyzer = TimeframeAnalyzer()

    result = analyzer.analyze(
        build_collection(),
    )

    assert result["shortest"].value is TimeframeType.M15
    assert result["longest"].value is TimeframeType.MN1