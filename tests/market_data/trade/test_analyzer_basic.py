"""
Tests for TradeAnalyzer basic functionality.
"""

from ogs.market_data.trade import (
    Trade,
    TradeAnalyzer,
    TradeCollection,
)


def make_trade(trade_id, price, quantity):

    return Trade(
        trade_id=trade_id,
        price=price,
        quantity=quantity,
    )


def test_analyzer_creation():

    collection = TradeCollection()

    analyzer = TradeAnalyzer(collection)

    assert analyzer.collection is collection


def test_summary():

    collection = TradeCollection()

    collection.add(make_trade("T1", 100, 10))
    collection.add(make_trade("T2", 200, 20))

    analyzer = TradeAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 2


def test_analyze():

    collection = TradeCollection()

    collection.add(make_trade("T1", 100, 10))

    analyzer = TradeAnalyzer(collection)

    result = analyzer.analyze()

    assert "summary" in result
    assert "trade_analysis" in result
    assert "distribution_analysis" in result