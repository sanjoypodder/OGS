"""
Tests for Broker factory.
"""

from ogs.market_data.broker import (
    Broker,
    BrokerFactory,
    BrokerStatus,
)


def test_create():

    broker = BrokerFactory.create(
        broker_id="BRK001",
        name="Broker One",
    )

    assert isinstance(broker, Broker)
    assert broker.broker_id == "BRK001"
    assert broker.name == "Broker One"


def test_active():

    broker = BrokerFactory.active(
        broker_id="BRK001",
        name="Broker One",
    )

    assert broker.status == BrokerStatus.ACTIVE


def test_inactive():

    broker = BrokerFactory.inactive(
        broker_id="BRK001",
        name="Broker One",
    )

    assert broker.status == BrokerStatus.INACTIVE


def test_clone():

    broker = BrokerFactory.create(
        broker_id="BRK001",
        name="Broker One",
    )

    clone = BrokerFactory.clone(broker)

    assert clone == broker
    assert clone is not broker