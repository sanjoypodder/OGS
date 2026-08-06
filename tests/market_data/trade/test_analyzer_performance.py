"""
Performance tests for TradeAnalyzer.
"""

from ogs.market_data.trade import (
    Trade,
    TradeAnalyzer,
    TradeCollection,
)


def test_large_collection():

    collection = TradeCollection()

    for i in range(1000):

        collection.add(
            Trade(
                trade_id=f"T{i}",
                price=100,
                quantity=1,
            )
        )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.summary()

    assert result["count"] == 1000


def test_large_analysis():

    collection = TradeCollection()

    for i in range(500):

        collection.add(
            Trade(
                trade_id=f"T{i}",
                price=200,
                quantity=2,
            )
        )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500
    assert result["trade_analysis"]["average_price"] == 200
    assert result["trade_analysis"]["average_quantity"] == 2