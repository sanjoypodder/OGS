"""
Tests for Market factory.
"""

from ogs.market_data.market import (
    Market,
    MarketFactory,
    MarketStatus,
)


def test_create():

    market = MarketFactory.create(
        market_id="INDIA",
        name="Indian Equity Market",
    )

    assert isinstance(market, Market)
    assert market.market_id == "INDIA"
    assert market.name == "Indian Equity Market"


def test_open():

    market = MarketFactory.open(
        market_id="INDIA",
        name="Indian Equity Market",
    )

    assert market.status == MarketStatus.OPEN


def test_closed():

    market = MarketFactory.closed(
        market_id="INDIA",
        name="Indian Equity Market",
    )

    assert market.status == MarketStatus.CLOSED


def test_clone():

    market = MarketFactory.create(
        market_id="INDIA",
        name="Indian Equity Market",
    )

    clone = MarketFactory.clone(market)

    assert clone == market
    assert clone is not market