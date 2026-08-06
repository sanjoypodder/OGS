"""
Tests for Broker domain.
"""

from ogs.market_data.broker import (
    Broker,
    BrokerStatus,
)


def test_default_broker():

    broker = Broker()

    assert broker.broker_id == ""
    assert broker.name == ""
    assert broker.country == ""
    assert broker.timezone == "UTC"
    assert broker.website == ""

    assert broker.status == BrokerStatus.UNKNOWN

    assert broker.account_count == 0
    assert broker.active_account_count == 0

    assert broker.total_equity == 0.0
    assert broker.total_cash == 0.0
    assert broker.total_buying_power == 0.0
    assert broker.total_margin_used == 0.0

    assert broker.supported_markets == []


def test_to_dict():

    broker = Broker()

    data = broker.to_dict()

    assert isinstance(data, dict)

    assert data["broker_id"] == ""
    assert data["account_count"] == 0


def test_str():

    broker = Broker()

    assert "Broker" in str(broker)


def test_is_active():

    broker = Broker(
        status=BrokerStatus.ACTIVE
    )

    assert broker.is_active


def test_is_valid():

    broker = Broker(
        broker_id="B1",
        name="Broker One",
    )

    assert broker.is_valid