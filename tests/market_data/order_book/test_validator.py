"""
Tests for OrderBook validator.
"""

from datetime import UTC
from datetime import datetime

import pytest

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookStatus,
    OrderBookType,
    OrderBookValidator,
)


validator = OrderBookValidator()


def test_validator_accepts_valid_orderbook():

    ob = OrderBook(
        name="BOOK",
        best_bid=100,
        best_ask=101,
    )

    assert validator(ob)


def test_validator_rejects_non_orderbook():

    with pytest.raises(TypeError):
        validator("invalid")


def test_validator_rejects_empty_name():

    with pytest.raises(ValueError):
        validator(OrderBook())


def test_negative_bid():

    with pytest.raises(ValueError):
        validator(
            OrderBook(
                name="BOOK",
                best_bid=-1,
            )
        )


def test_negative_ask():

    with pytest.raises(ValueError):
        validator(
            OrderBook(
                name="BOOK",
                best_ask=-1,
            )
        )


def test_bid_greater_than_ask():

    with pytest.raises(ValueError):
        validator(
            OrderBook(
                name="BOOK",
                best_bid=105,
                best_ask=100,
            )
        )


def test_invalid_orderbook_type():

    ob = OrderBook(name="BOOK")

    ob.orderbook_type = "LIVE"

    with pytest.raises(ValueError):
        validator(ob)


def test_invalid_status():

    ob = OrderBook(name="BOOK")

    ob.status = "ACTIVE"

    with pytest.raises(ValueError):
        validator(ob)


def test_invalid_timestamp():

    ob = OrderBook(name="BOOK")

    ob.timestamp = "today"

    with pytest.raises(ValueError):
        validator(ob)


def test_callable_validator():

    ob = OrderBook(
        name="BOOK",
        best_bid=1,
        best_ask=2,
    )

    assert validator(ob)


def test_valid_enums():

    assert isinstance(
        OrderBookType.LIVE,
        OrderBookType,
    )

    assert isinstance(
        OrderBookStatus.ACTIVE,
        OrderBookStatus,
    )


def test_valid_datetime():

    assert isinstance(
        datetime.now(UTC),
        datetime,
    )