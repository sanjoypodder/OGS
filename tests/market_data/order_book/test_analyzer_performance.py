"""
Performance tests for OrderBookAnalyzer.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookAnalyzer,
    OrderBookCollection,
)


def test_large_collection():

    collection = OrderBookCollection()

    for i in range(1000):

        collection.add(
            OrderBook(
                name=f"OB{i}",
                best_bid=float(i),
                best_ask=float(i + 1),
            )
        )

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.summary()

    assert result["count"] == 1000


def test_large_analysis():

    collection = OrderBookCollection()

    for i in range(500):

        collection.add(
            OrderBook(
                name=f"OB{i}",
                best_bid=float(i),
                best_ask=float(i + 2),
            )
        )

    analyzer = OrderBookAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500
    assert result["spread_analysis"]["average_spread"] == 2.0