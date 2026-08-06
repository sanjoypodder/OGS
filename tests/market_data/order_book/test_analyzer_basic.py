"""
Tests for OrderBookAnalyzer basic functionality.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookAnalyzer,
    OrderBookCollection,
)


def make_book(name, bid, ask):

    return OrderBook(
        name=name,
        best_bid=bid,
        best_ask=ask,
    )


def test_analyzer_creation():

    collection = OrderBookCollection()

    analyzer = OrderBookAnalyzer(collection)

    assert analyzer.collection is collection


def test_summary():

    collection = OrderBookCollection()

    collection.add(make_book("A", 100, 101))
    collection.add(make_book("B", 200, 201))

    analyzer = OrderBookAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 2


def test_analyze():

    collection = OrderBookCollection()

    collection.add(make_book("ABC", 100, 101))

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.analyze()

    assert "summary" in result
    assert "spread_analysis" in result
    assert "distribution_analysis" in result
    assert "imbalance_analysis" in result