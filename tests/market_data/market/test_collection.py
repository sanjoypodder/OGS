"""
Tests for Market collection.
"""

from ogs.market_data.market import (
    Market,
    MarketCollection,
    MarketStatus,
)


def make_market(i):

    return Market(
        market_id=f"MKT{i}",
        name=f"Market {i}",
        status=MarketStatus.OPEN,
    )


def test_collection():

    collection = MarketCollection()

    assert len(collection) == 0

    collection.add(make_market(1))

    assert len(collection) == 1


def test_find():

    collection = MarketCollection()

    market = make_market(1)

    collection.add(market)

    assert collection.find("MKT1") == market
    assert collection.find("UNKNOWN") is None


def test_filters():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="OPEN",
            name="Open Market",
            status=MarketStatus.OPEN,
        )
    )

    collection.add(
        Market(
            market_id="CLOSED",
            name="Closed Market",
            status=MarketStatus.CLOSED,
        )
    )

    assert len(collection.open()) == 1
    assert len(collection.closed()) == 1


def test_totals():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Market",
        )
    )

    assert collection.total_exchanges() == 0
    assert collection.total_brokers() == 0
    assert collection.total_accounts() == 0
    assert collection.total_equity() == 0.0
    assert collection.total_cash() == 0.0
    assert collection.total_buying_power() == 0.0
    assert collection.total_margin_used() == 0.0


def test_to_list():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Market",
        )
    )

    data = collection.to_list()

    assert isinstance(data, list)
    assert len(data) == 1