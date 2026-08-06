"""
Performance tests for Market analyzer.
"""

from ogs.market_data.market import (
    Market,
    MarketAnalyzer,
    MarketCollection,
)


def test_large_collection():

    collection = MarketCollection()

    for i in range(1000):

        collection.add(
            Market(
                market_id=f"MKT{i}",
                name=f"Market {i}",
            )
        )

    analyzer = MarketAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 1000


def test_summary_speed():

    collection = MarketCollection()

    for i in range(500):

        collection.add(
            Market(
                market_id=str(i),
                name=f"Market {i}",
            )
        )

    analyzer = MarketAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 500