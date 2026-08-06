"""
Performance tests for QuoteAnalyzer.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteAnalyzer,
    QuoteCollection,
)


def test_large_collection():

    collection = QuoteCollection()

    for i in range(1000):

        collection.add(
            Quote(
                name=f"Q{i}",
                bid=float(i),
                ask=float(i + 1),
            )
        )

    analyzer = QuoteAnalyzer(collection)

    result = analyzer.summary()

    assert result["count"] == 1000


def test_large_analysis():

    collection = QuoteCollection()

    for i in range(500):

        collection.add(
            Quote(
                name=f"Q{i}",
                bid=float(i),
                ask=float(i + 2),
            )
        )

    analyzer = QuoteAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500
    assert result["spread_analysis"]["average_spread"] == 2.0