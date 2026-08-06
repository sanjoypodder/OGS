"""
Tests for SymbolCollection.
"""

from ogs.market_data.symbol import (
    Currency,
    Exchange,
    SymbolCollection,
    SymbolFactory,
)


def create_collection():

    collection = SymbolCollection()

    collection.append(
        SymbolFactory.forex(
            "EURUSD",
            Currency.EUR,
            Currency.USD,
        )
    )

    collection.append(
        SymbolFactory.crypto(
            "BTCUSDT",
            Currency.BTC,
        )
    )

    collection.append(
        SymbolFactory.stock(
            "TCS",
            "Tata Consultancy Services",
        )
    )

    return collection


def test_append():

    collection = create_collection()

    assert len(collection) == 3


def test_forex():

    collection = create_collection()

    assert len(collection.forex()) == 1


def test_crypto():

    collection = create_collection()

    assert len(collection.crypto()) == 1


def test_stock():

    collection = create_collection()

    assert len(collection.stocks()) == 1


def test_find():

    collection = create_collection()

    symbol = collection.find("EURUSD")

    assert symbol is not None
    assert symbol.symbol == "EURUSD"


def test_find_lowercase():

    collection = create_collection()

    symbol = collection.find("eurusd")

    assert symbol is not None
    assert symbol.symbol == "EURUSD"


def test_find_missing():

    collection = create_collection()

    assert collection.find("ABC") is None


def test_by_exchange():

    collection = create_collection()

    forex = collection.by_exchange(
        Exchange.FOREX
    )

    assert len(forex) == 1


def test_active():

    collection = create_collection()

    assert len(collection.active()) == 3


def test_inactive():

    collection = create_collection()

    assert len(collection.inactive()) == 0