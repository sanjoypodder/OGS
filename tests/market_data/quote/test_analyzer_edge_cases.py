"""
Edge case tests for QuoteAnalyzer.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteAnalyzer,
    QuoteCollection,
)


def test_empty_collection():

    collection = QuoteCollection()

    analyzer = QuoteAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_single_quote():

    collection = QuoteCollection()

    collection.add(
        Quote(
            name="ABC",
            bid=10,
            ask=11,
        )
    )

    analyzer = QuoteAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1


def test_zero_spread():

    collection = QuoteCollection()

    collection.add(
        Quote(
            name="ABC",
            bid=100,
            ask=100,
        )
    )

    analyzer = QuoteAnalyzer(collection)

    spread = analyzer.spread_analysis()

    assert spread["average_spread"] == 0.0