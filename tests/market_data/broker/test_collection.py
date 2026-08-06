"""
Tests for Broker collection.
"""

from ogs.market_data.broker import (
    Broker,
    BrokerCollection,
    BrokerStatus,
)


def make_broker(i):

    return Broker(
        broker_id=f"B{i}",
        name=f"Broker {i}",
        status=BrokerStatus.ACTIVE,
    )


def test_collection():

    collection = BrokerCollection()

    assert len(collection) == 0

    collection.add(make_broker(1))

    assert len(collection) == 1


def test_find():

    collection = BrokerCollection()

    broker = make_broker(1)

    collection.add(broker)

    assert collection.find("B1") == broker
    assert collection.find("UNKNOWN") is None


def test_filters():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="1",
            name="Active",
            status=BrokerStatus.ACTIVE,
        )
    )

    collection.add(
        Broker(
            broker_id="2",
            name="Inactive",
            status=BrokerStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1
    assert len(collection.inactive()) == 1


def test_totals():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="1",
            name="Broker",
        )
    )

    assert collection.total_accounts() == 0
    assert collection.total_equity() == 0.0
    assert collection.total_cash() == 0.0
    assert collection.total_buying_power() == 0.0
    assert collection.total_margin_used() == 0.0


def test_to_list():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="1",
            name="Broker",
        )
    )

    data = collection.to_list()

    assert isinstance(data, list)
    assert len(data) == 1