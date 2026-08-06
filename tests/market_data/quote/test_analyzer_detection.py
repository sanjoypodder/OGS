"""
Detection tests for QuoteAnalyzer.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteAnalyzer,
    QuoteCollection,
)


def test_average_spread_detection():

    collection = QuoteCollection()

    collection.add(
        Quote(
            name="A",
            bid=100,
            ask=102,
        )
    )

    collection.add(
        Quote(
            name="B",
            bid=200,
            ask=204,
        )
    )

    analyzer = QuoteAnalyzer(collection)

    result = analyzer.spread_analysis()

    assert result["average_spread"] == 3.0


def test_distribution_detection():

    collection = QuoteCollection()

    collection.add(Quote(name="ONE"))

    analyzer = QuoteAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert "types" in result
    assert "status" in result
    assert "providers" in result