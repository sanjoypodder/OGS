"""
===========================================================

OGS Smart Money AI

Order Block Domain Tests

===========================================================
"""

from dataclasses import FrozenInstanceError

import pytest

from tests.factories import (
    make_bullish_order_block,
)


def test_create():

    ob = make_bullish_order_block()

    assert ob is not None


def test_timestamp():

    ob = make_bullish_order_block()

    assert ob.timestamp == ob.origin_candle.timestamp


def test_high():

    ob = make_bullish_order_block()

    assert ob.high == ob.origin_candle.high


def test_low():

    ob = make_bullish_order_block()

    assert ob.low == ob.origin_candle.low


def test_open():

    ob = make_bullish_order_block()

    assert ob.open == ob.origin_candle.open


def test_close():

    ob = make_bullish_order_block()

    assert ob.close == ob.origin_candle.close


def test_string():

    ob = make_bullish_order_block()

    assert "Order Block" in str(ob)


def test_frozen():

    ob = make_bullish_order_block()

    with pytest.raises(FrozenInstanceError):
        ob.direction = None