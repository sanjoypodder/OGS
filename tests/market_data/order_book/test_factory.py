"""
Tests for OrderBookFactory.
"""

import pytest

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookFactory,
    OrderBookType,
)


def test_create():

    ob = OrderBookFactory.create(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    assert isinstance(ob, OrderBook)


def test_live_factory():

    ob = OrderBookFactory.live(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    assert ob.orderbook_type == OrderBookType.LIVE


def test_historical_factory():

    ob = OrderBookFactory.historical(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    assert ob.orderbook_type == OrderBookType.HISTORICAL


def test_simulated_factory():

    ob = OrderBookFactory.simulated(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    assert ob.orderbook_type == OrderBookType.SIMULATED


def test_clone():

    ob = OrderBookFactory.create(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    clone = OrderBookFactory.clone(ob)

    assert clone == ob
    assert clone is not ob


def test_clone_independent():

    ob = OrderBookFactory.create(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    clone = OrderBookFactory.clone(ob)

    clone.best_bid = 50

    assert ob.best_bid == 100


def test_factory_validation():

    with pytest.raises(ValueError):

        OrderBookFactory.create(
            name="BOOK",
            best_bid=105,
            best_ask=100,
        )