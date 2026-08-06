"""
Tests for Exchange validator.
"""

import pytest

from ogs.market_data.exchange import (
    Exchange,
    ExchangeStatus,
    ExchangeValidator,
    TradingSession,
)


def valid_exchange():

    return Exchange(
        exchange_id="NSE",
        name="National Stock Exchange",
        session=TradingSession.REGULAR,
        status=ExchangeStatus.OPEN,
    )


def test_validator_success():

    validator = ExchangeValidator()

    assert validator(valid_exchange())


@pytest.mark.parametrize(
    "field,value",
    [
        ("exchange_id", ""),
        ("name", ""),
    ],
)
def test_required_fields(
    field,
    value,
):

    exchange = valid_exchange()

    setattr(
        exchange,
        field,
        value,
    )

    with pytest.raises(ValueError):
        ExchangeValidator()(exchange)


def test_invalid_session():

    exchange = valid_exchange()

    exchange.session = "REGULAR"

    with pytest.raises(ValueError):
        ExchangeValidator()(exchange)


def test_invalid_status():

    exchange = valid_exchange()

    exchange.status = "OPEN"

    with pytest.raises(ValueError):
        ExchangeValidator()(exchange)


def test_invalid_created_at():

    exchange = valid_exchange()

    exchange.created_at = None

    with pytest.raises(ValueError):
        ExchangeValidator()(exchange)


def test_invalid_updated_at():

    exchange = valid_exchange()

    exchange.updated_at = None

    with pytest.raises(ValueError):
        ExchangeValidator()(exchange)