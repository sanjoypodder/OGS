"""
Detection tests for OrderBookAnalyzer.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookAnalyzer,
    OrderBookCollection,
)


def test_average_spread_detection():

    collection = OrderBookCollection()

    collection.add(
        OrderBook(
            name="A",
            best_bid=100,
            best_ask=102,
        )
    )

    collection.add(
        OrderBook(
            name="B",
            best_bid=200,
            best_ask=204,
        )
    )

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.spread_analysis()

    assert result["average_spread"] == 3.0


def test_distribution_detection():

    collection = OrderBookCollection()

    collection.add(OrderBook(name="ONE"))

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert "types" in result
    assert "status" in result
    assert "providers" in result


def test_imbalance_detection():

    collection = OrderBookCollection()

    collection.add(
        OrderBook(
            name="BOOK",
            bid_levels=[(100, 30)],
            ask_levels=[(101, 10)],
        )
    )

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.imbalance_analysis()

    assert result["average_imbalance"] == 0.75