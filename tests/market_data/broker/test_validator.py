"""
Tests for Broker validator.
"""

import pytest

from ogs.market_data.broker import (
    Broker,
    BrokerStatus,
    BrokerValidator,
    MarketType,
)


def valid_broker():

    return Broker(
        broker_id="BRK001",
        name="Broker One",
        status=BrokerStatus.ACTIVE,
        supported_markets=[
            MarketType.EQUITY,
            MarketType.FOREX,
        ],
    )


def test_validator_success():

    validator = BrokerValidator()

    assert validator(valid_broker())


@pytest.mark.parametrize(
    "field,value",
    [
        ("broker_id", ""),
        ("name", ""),
    ],
)
def test_required_fields(
    field,
    value,
):

    broker = valid_broker()

    setattr(
        broker,
        field,
        value,
    )

    with pytest.raises(ValueError):
        BrokerValidator()(broker)


def test_invalid_status():

    broker = valid_broker()

    broker.status = "ACTIVE"

    with pytest.raises(ValueError):
        BrokerValidator()(broker)


def test_invalid_market_type():

    broker = valid_broker()

    broker.supported_markets.append(
        "INVALID"
    )

    with pytest.raises(ValueError):
        BrokerValidator()(broker)


def test_invalid_created_at():

    broker = valid_broker()

    broker.created_at = None

    with pytest.raises(ValueError):
        BrokerValidator()(broker)


def test_invalid_updated_at():

    broker = valid_broker()

    broker.updated_at = None

    with pytest.raises(ValueError):
        BrokerValidator()(broker)