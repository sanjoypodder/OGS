"""
Tests for Market domain.
"""

from ogs.market_data.market import (
    Market,
    MarketStatus,
    MarketType,
)


def test_default_market():

    market = Market()

    assert market.market_id == ""
    assert market.name == ""
    assert market.country == ""
    assert market.currency == "USD"
    assert market.timezone == "UTC"

    assert market.market_type == MarketType.EQUITY
    assert market.status == MarketStatus.UNKNOWN

    assert market.exchange_count == 0
    assert market.broker_count == 0
    assert market.account_count == 0

    assert market.total_equity == 0.0
    assert market.total_cash == 0.0
    assert market.total_buying_power == 0.0
    assert market.total_margin_used == 0.0


def test_to_dict():

    market = Market()

    data = market.to_dict()

    assert isinstance(data, dict)

    assert data["market_id"] == ""
    assert data["exchange_count"] == 0


def test_str():

    market = Market()

    assert "Market" in str(market)


def test_is_open():

    market = Market(
        status=MarketStatus.OPEN,
    )

    assert market.is_open


def test_is_valid():

    market = Market(
        market_id="INDIA",
        name="Indian Equity Market",
    )

    assert market.is_valid