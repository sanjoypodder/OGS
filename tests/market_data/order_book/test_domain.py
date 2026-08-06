"""
Tests for OrderBook domain.
"""

from datetime import UTC
from datetime import datetime

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookType,
)


def test_default_orderbook():

    ob = OrderBook()

    assert ob.name == ""
    assert ob.best_bid == 0.0
    assert ob.best_ask == 0.0
    assert ob.bid_levels == []
    assert ob.ask_levels == []


def test_spread():

    ob = OrderBook(
        best_bid=100,
        best_ask=101,
    )

    assert ob.spread == 1


def test_mid_price():

    ob = OrderBook(
        best_bid=100,
        best_ask=102,
    )

    assert ob.mid_price == 101


def test_mid_price_zero():

    ob = OrderBook()

    assert ob.mid_price == 0.0


def test_bid_volume():

    ob = OrderBook(
        bid_levels=[
            (100, 10),
            (99, 20),
        ]
    )

    assert ob.total_bid_volume == 30


def test_ask_volume():

    ob = OrderBook(
        ask_levels=[
            (101, 5),
            (102, 15),
        ]
    )

    assert ob.total_ask_volume == 20


def test_imbalance_ratio():

    ob = OrderBook(
        bid_levels=[
            (100, 30),
        ],
        ask_levels=[
            (101, 10),
        ],
    )

    assert ob.imbalance_ratio == 0.75


def test_live_property():

    ob = OrderBook(
        orderbook_type=OrderBookType.LIVE
    )

    assert ob.is_live


def test_valid_orderbook():

    ob = OrderBook(
        best_bid=100,
        best_ask=101,
    )

    assert ob.is_valid


def test_invalid_orderbook():

    ob = OrderBook(
        best_bid=105,
        best_ask=100,
    )

    assert not ob.is_valid


def test_to_dict():

    ob = OrderBook(name="BOOK")

    d = ob.to_dict()

    assert d["name"] == "BOOK"


def test_timestamp():

    ob = OrderBook()

    assert isinstance(
        ob.timestamp,
        datetime,
    )


def test_custom_timestamp():

    ts = datetime.now(UTC)

    ob = OrderBook(timestamp=ts)

    assert ob.timestamp == ts


def test_string():

    ob = OrderBook(name="BOOK")

    assert "BOOK" in str(ob)