"""
Edge case tests for OrderBookAnalyzer.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookAnalyzer,
    OrderBookCollection,
)


def test_empty_collection():

    collection = OrderBookCollection()

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_single_orderbook():

    collection = OrderBookCollection()

    collection.add(
        OrderBook(
            name="ABC",
            best_bid=10,
            best_ask=11,
        )
    )

    analyzer = OrderBookAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1


def test_zero_spread():

    collection = OrderBookCollection()

    collection.add(
        OrderBook(
            name="ABC",
            best_bid=100,
            best_ask=100,
        )
    )

    analyzer = OrderBookAnalyzer(collection)

    spread = analyzer.spread_analysis()

    assert spread["average_spread"] == 0.0


def test_zero_imbalance():

    collection = OrderBookCollection()

    collection.add(OrderBook(name="BOOK"))

    analyzer = OrderBookAnalyzer(collection)

    imbalance = analyzer.imbalance_analysis()

    assert imbalance["average_imbalance"] == 0.0