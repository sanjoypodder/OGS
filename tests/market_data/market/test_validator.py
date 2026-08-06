"""
Tests for Market validator.
"""

import pytest

from ogs.market_data.market import (
    Market,
    MarketStatus,
    MarketType,
    MarketValidator,
)


def valid_market():

    return Market(
        market_id="INDIA",
        name="Indian Equity Market",
        market_type=MarketType.EQUITY,
        status=MarketStatus.OPEN,
    )


def test_validator_success():

    validator = MarketValidator()

    assert validator(valid_market())


@pytest.mark.parametrize(
    "field,value",
    [
        ("market_id", ""),
        ("name", ""),
    ],
)
def test_required_fields(
    field,
    value,
):

    market = valid_market()

    setattr(
        market,
        field,
        value,
    )

    with pytest.raises(ValueError):
        MarketValidator()(market)


def test_invalid_market_type():

    market = valid_market()

    market.market_type = "EQUITY"

    with pytest.raises(ValueError):
        MarketValidator()(market)


def test_invalid_status():

    market = valid_market()

    market.status = "OPEN"

    with pytest.raises(ValueError):
        MarketValidator()(market)


def test_invalid_created_at():

    market = valid_market()

    market.created_at = None

    with pytest.raises(ValueError):
        MarketValidator()(market)


def test_invalid_updated_at():

    market = valid_market()

    market.updated_at = None

    with pytest.raises(ValueError):
        MarketValidator()(market)