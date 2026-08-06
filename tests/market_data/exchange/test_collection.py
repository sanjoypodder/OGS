"""
Tests for Exchange collection.
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeCollection,
    ExchangeStatus,
)


def make_exchange(i):

    return Exchange(
        exchange_id=f"EX{i}",
        name=f"Exchange {i}",
        status=ExchangeStatus.OPEN,
    )


def test_collection():

    collection = ExchangeCollection()

    assert len(collection) == 0

    collection.add(make_exchange(1))

    assert len(collection) == 1


def test_find():

    collection = ExchangeCollection()

    exchange = make_exchange(1)

    collection.add(exchange)

    assert collection.find("EX1") == exchange
    assert collection.find("UNKNOWN") is None


def test_filters():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="1",
            name="Open",
            status=ExchangeStatus.OPEN,
        )
    )

    collection.add(
        Exchange(
            exchange_id="2",
            name="Closed",
            status=ExchangeStatus.CLOSED,
        )
    )

    assert len(collection.open()) == 1
    assert len(collection.closed()) == 1


def test_totals():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="1",
            name="Exchange",
        )
    )

    assert collection.total_brokers() == 0
    assert collection.total_accounts() == 0
    assert collection.total_equity() == 0.0
    assert collection.total_cash() == 0.0
    assert collection.total_buying_power() == 0.0
    assert collection.total_margin_used() == 0.0


def test_to_list():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="1",
            name="Exchange",
        )
    )

    data = collection.to_list()

    assert isinstance(data, list)
    assert len(data) == 1