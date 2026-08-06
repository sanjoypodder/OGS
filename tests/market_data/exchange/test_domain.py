"""
Tests for Exchange domain.
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeStatus,
    TradingSession,
)


def test_default_exchange():

    exchange = Exchange()

    assert exchange.exchange_id == ""
    assert exchange.name == ""
    assert exchange.mic == ""
    assert exchange.country == ""
    assert exchange.timezone == "UTC"
    assert exchange.currency == "USD"

    assert exchange.session == TradingSession.REGULAR
    assert exchange.status == ExchangeStatus.UNKNOWN

    assert exchange.broker_count == 0
    assert exchange.active_broker_count == 0
    assert exchange.account_count == 0

    assert exchange.total_equity == 0.0
    assert exchange.total_cash == 0.0
    assert exchange.total_buying_power == 0.0
    assert exchange.total_margin_used == 0.0


def test_to_dict():

    exchange = Exchange()

    data = exchange.to_dict()

    assert isinstance(data, dict)

    assert data["exchange_id"] == ""
    assert data["broker_count"] == 0


def test_str():

    exchange = Exchange()

    assert "Exchange" in str(exchange)


def test_is_open():

    exchange = Exchange(
        status=ExchangeStatus.OPEN
    )

    assert exchange.is_open


def test_is_valid():

    exchange = Exchange(
        exchange_id="NSE",
        name="National Stock Exchange",
    )

    assert exchange.is_valid