"""
Detection tests for TradeAnalyzer.
"""

from ogs.market_data.trade import (
    Trade,
    TradeAnalyzer,
    TradeCollection,
    TradeSide,
)


def test_trade_analysis():

    collection = TradeCollection()

    collection.add(
        Trade(
            trade_id="BUY1",
            side=TradeSide.BUY,
            price=100,
            quantity=5,
        )
    )

    collection.add(
        Trade(
            trade_id="SELL1",
            side=TradeSide.SELL,
            price=200,
            quantity=2,
        )
    )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.trade_analysis()

    assert result["buy_count"] == 1
    assert result["sell_count"] == 1


def test_distribution_analysis():

    collection = TradeCollection()

    collection.add(
        Trade(
            trade_id="T1",
            provider="NSE",
            symbol="NIFTY",
        )
    )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert "providers" in result
    assert "symbols" in result


def test_total_value_detection():

    collection = TradeCollection()

    collection.add(
        Trade(
            trade_id="T1",
            price=100,
            quantity=5,
        )
    )

    analyzer = TradeAnalyzer(collection)

    result = analyzer.trade_analysis()

    assert result["total_value"] == 500