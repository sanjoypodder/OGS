"""
Tests for TradeCollection.
"""

from ogs.market_data.trade import (
    Trade,
    TradeCollection,
    TradeSide,
    TradeStatus,
)


def make_trade(
    trade_id,
    side=TradeSide.BUY,
    status=TradeStatus.FILLED,
    symbol="NIFTY",
    provider="NSE",
):

    return Trade(
        trade_id=trade_id,
        side=side,
        status=status,
        symbol=symbol,
        provider=provider,
        price=100,
        quantity=10,
        fees=1,
    )


def test_add():

    collection = TradeCollection()

    trade = make_trade("T1")

    collection.add(trade)

    assert len(collection.items) == 1


def test_buys():

    collection = TradeCollection()

    collection.add(make_trade("B1", side=TradeSide.BUY))
    collection.add(make_trade("S1", side=TradeSide.SELL))

    assert len(collection.buys()) == 1


def test_sells():

    collection = TradeCollection()

    collection.add(make_trade("B1", side=TradeSide.BUY))
    collection.add(make_trade("S1", side=TradeSide.SELL))

    assert len(collection.sells()) == 1


def test_filled():

    collection = TradeCollection()

    collection.add(make_trade("A"))

    collection.add(
        make_trade(
            "B",
            status=TradeStatus.PENDING,
        )
    )

    assert len(collection.filled()) == 1


def test_by_symbol():

    collection = TradeCollection()

    collection.add(make_trade("A", symbol="AAPL"))
    collection.add(make_trade("B", symbol="MSFT"))

    assert len(collection.by_symbol("AAPL")) == 1


def test_by_provider():

    collection = TradeCollection()

    collection.add(make_trade("A", provider="NSE"))
    collection.add(make_trade("B", provider="BSE"))

    assert len(collection.by_provider("NSE")) == 1


def test_find():

    collection = TradeCollection()

    trade = make_trade("ABC")

    collection.add(trade)

    assert collection.find("ABC") is trade


def test_total_value():

    collection = TradeCollection()

    collection.add(make_trade("A"))
    collection.add(make_trade("B"))

    assert collection.total_value() == 2000


def test_total_fees():

    collection = TradeCollection()

    collection.add(make_trade("A"))
    collection.add(make_trade("B"))

    assert collection.total_fees() == 2


def test_to_list():

    collection = TradeCollection()

    collection.add(make_trade("A"))

    assert len(collection.to_list()) == 1