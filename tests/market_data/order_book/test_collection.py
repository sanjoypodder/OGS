"""
Tests for OrderBookCollection.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookCollection,
    OrderBookStatus,
    OrderBookType,
)


def make_book(
    name,
    provider="NSE",
    symbol="NIFTY",
    status=OrderBookStatus.ACTIVE,
    orderbook_type=OrderBookType.LIVE,
):

    return OrderBook(
        name=name,
        provider=provider,
        symbol=symbol,
        status=status,
        orderbook_type=orderbook_type,
    )


def test_add():

    c = OrderBookCollection()

    b = make_book("A")

    c.add(b)

    assert len(c.items) == 1


def test_active():

    c = OrderBookCollection()

    c.add(make_book("A"))
    c.add(make_book("B", status=OrderBookStatus.CLOSED))

    assert len(c.active()) == 1


def test_inactive():

    c = OrderBookCollection()

    c.add(make_book("A"))
    c.add(make_book("B", status=OrderBookStatus.CLOSED))

    assert len(c.inactive()) == 1


def test_by_type():

    c = OrderBookCollection()

    c.add(make_book("A"))
    c.add(
        make_book(
            "B",
            orderbook_type=OrderBookType.HISTORICAL,
        )
    )

    assert len(c.by_type(OrderBookType.LIVE)) == 1


def test_by_provider():

    c = OrderBookCollection()

    c.add(make_book("A", provider="NSE"))
    c.add(make_book("B", provider="BSE"))

    assert len(c.by_provider("NSE")) == 1


def test_by_symbol():

    c = OrderBookCollection()

    c.add(make_book("A", symbol="AAPL"))
    c.add(make_book("B", symbol="MSFT"))

    assert len(c.by_symbol("AAPL")) == 1


def test_find():

    c = OrderBookCollection()

    b = make_book("ABC")

    c.add(b)

    assert c.find("ABC") is b


def test_total_active():

    c = OrderBookCollection()

    c.add(make_book("A"))
    c.add(make_book("B"))

    assert c.total_active() == 2


def test_to_list():

    c = OrderBookCollection()

    c.add(make_book("A"))

    assert len(c.to_list()) == 1