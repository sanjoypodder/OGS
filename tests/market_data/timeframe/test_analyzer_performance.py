"""
Performance tests for TimeframeAnalyzer.
"""

from ogs.market_data.timeframe import (
    TimeframeAnalyzer,
    TimeframeCollection,
    TimeframeFactory,
    TimeframeType,
)


def test_large_collection():

    analyzer = TimeframeAnalyzer()

    collection = TimeframeCollection()

    for _ in range(5000):

        collection.append(
            TimeframeFactory.create(
                TimeframeType.M15,
            )
        )

    assert len(analyzer.intraday(collection)) == 5000
    assert analyzer.average_minutes(collection) == 15.0


def test_large_analysis():

    analyzer = TimeframeAnalyzer()

    collection = TimeframeCollection()

    for _ in range(2500):

        collection.append(
            TimeframeFactory.create(
                TimeframeType.D1,
            )
        )

    result = analyzer.analyze(collection)

    assert result["count"] == 2500
    assert result["intraday"] == 0
    assert result["higher"] == 2500