"""
Tests for QuoteAnalyzer basic functionality.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteAnalyzer,
    QuoteCollection,
)


def make_quote(name, bid, ask):

    return Quote(
        name=name,
        bid=bid,
        ask=ask,
        last=(bid + ask) / 2,
    )


def test_analyzer_creation():

    collection = QuoteCollection()

    analyzer = QuoteAnalyzer(collection)

    assert analyzer.collection is collection


def test_summary():

    collection = QuoteCollection()

    collection.add(make_quote("A", 100, 101))
    collection.add(make_quote("B", 200, 201))

    analyzer = QuoteAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 2


def test_analyze():

    collection = QuoteCollection()

    collection.add(make_quote("ABC", 100, 101))

    analyzer = QuoteAnalyzer(collection)

    result = analyzer.analyze()

    assert "summary" in result
    assert "spread_analysis" in result
    assert "distribution_analysis" in result