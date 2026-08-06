"""
Tests for Exchange factory.
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeFactory,
    ExchangeStatus,
)


def test_create():

    exchange = ExchangeFactory.create(
        exchange_id="NSE",
        name="National Stock Exchange",
    )

    assert isinstance(exchange, Exchange)
    assert exchange.exchange_id == "NSE"
    assert exchange.name == "National Stock Exchange"


def test_open():

    exchange = ExchangeFactory.open(
        exchange_id="NSE",
        name="NSE",
    )

    assert exchange.status == ExchangeStatus.OPEN


def test_closed():

    exchange = ExchangeFactory.closed(
        exchange_id="NSE",
        name="NSE",
    )

    assert exchange.status == ExchangeStatus.CLOSED


def test_clone():

    exchange = ExchangeFactory.create(
        exchange_id="NSE",
        name="NSE",
    )

    clone = ExchangeFactory.clone(exchange)

    assert clone == exchange
    assert clone is not exchange