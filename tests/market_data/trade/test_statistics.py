"""
Tests for TradeStatistics.
"""

from ogs.market_data.trade import (
    Trade,
    TradeCollection,
    TradeSide,
    TradeStatistics,
)


def make_trade(
    trade_id,
    side=TradeSide.BUY,
    provider="NSE",
    symbol="NIFTY",
):

    return Trade(
        trade_id=trade_id,
        side=side,
        provider=provider,
        symbol=symbol,
        price=100,
        quantity=10,
        fees=2,
    )


def test_count():

    collection = TradeCollection()

    collection.add(make_trade("A"))

    stats = TradeStatistics(collection)

    assert stats.count == 1


def test_buy_sell_count():

    collection = TradeCollection()

    collection.add(make_trade("A", side=TradeSide.BUY))
    collection.add(make_trade("B", side=TradeSide.SELL))

    stats = TradeStatistics(collection)

    assert stats.buy_count == 1
    assert stats.sell_count == 1


def test_total_value():

    collection = TradeCollection()

    collection.add(make_trade("A"))
    collection.add(make_trade("B"))

    stats = TradeStatistics(collection)

    assert stats.total_value == 2000


def test_total_fees():

    collection = TradeCollection()

    collection.add(make_trade("A"))
    collection.add(make_trade("B"))

    stats = TradeStatistics(collection)

    assert stats.total_fees == 4


def test_average_price():

    collection = TradeCollection()

    collection.add(make_trade("A"))
    collection.add(make_trade("B"))

    stats = TradeStatistics(collection)

    assert stats.average_price == 100


def test_average_quantity():

    collection = TradeCollection()

    collection.add(make_trade("A"))
    collection.add(make_trade("B"))

    stats = TradeStatistics(collection)

    assert stats.average_quantity == 10


def test_provider_distribution():

    collection = TradeCollection()

    collection.add(make_trade("A", provider="NSE"))

    stats = TradeStatistics(collection)

    assert stats.provider_distribution["NSE"] == 1


def test_symbol_distribution():

    collection = TradeCollection()

    collection.add(make_trade("A", symbol="BANKNIFTY"))

    stats = TradeStatistics(collection)

    assert stats.symbol_distribution["BANKNIFTY"] == 1


def test_summary():

    collection = TradeCollection()

    collection.add(make_trade("A"))

    stats = TradeStatistics(collection)

    summary = stats.summary()

    assert summary["count"] == 1


def test_empty_statistics():

    collection = TradeCollection()

    stats = TradeStatistics(collection)

    assert stats.average_price == 0.0
    assert stats.average_quantity == 0.0