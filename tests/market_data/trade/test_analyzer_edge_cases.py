"""
Edge case tests for TradeAnalyzer.
"""

from ogs.market_data.trade import (
    Trade,
    TradeAnalyzer,
    TradeCollection,
)


def test_empty_collection():

    collection = TradeCollection()

    analyzer = TradeAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_single_trade():

    collection = TradeCollection()

    collection.add(
        Trade(
            trade_id="T1",
            price=100,
            quantity=1,
        )
    )

    analyzer = TradeAnalyzer(collection)

    assert analyzer.summary()["count"] == 1


def test_zero_value_trade():

    collection = TradeCollection()

    collection.add(
        Trade(
            trade_id="T1",
            price=0,
            quantity=0,
        )
    )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.trade_analysis()

    assert result["total_value"] == 0


def test_zero_fees():

    collection = TradeCollection()

    collection.add(
        Trade(
            trade_id="T1",
            price=100,
            quantity=10,
            fees=0,
        )
    )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.trade_analysis()

    assert result["total_fees"] == 0