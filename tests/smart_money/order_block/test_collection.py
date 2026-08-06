"""
===========================================================

OGS Smart Money AI

Order Block Collection Tests

===========================================================
"""

from tests.factories import (
    make_bullish_order_block,
)

from ogs.smart_money.order_block import (
    OrderBlockSeries,
)


def test_create():

    series = OrderBlockSeries([])

    assert len(series) == 0


def test_append():

    series = OrderBlockSeries([])

    series.append(
        make_bullish_order_block()
    )

    assert len(series) == 1


def test_first():

    ob = make_bullish_order_block()

    series = OrderBlockSeries([ob])

    assert series.first == ob


def test_last():

    ob = make_bullish_order_block()

    series = OrderBlockSeries([ob])

    assert series.last == ob


def test_latest():

    ob = make_bullish_order_block()

    series = OrderBlockSeries([ob])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == ob


def test_iteration():

    ob = make_bullish_order_block()

    series = OrderBlockSeries([ob])

    assert list(series)[0] == ob


def test_indexing():

    ob = make_bullish_order_block()

    series = OrderBlockSeries([ob])

    assert series[0] == ob


def test_is_empty():

    series = OrderBlockSeries([])

    assert series.is_empty


def test_not_empty():

    series = OrderBlockSeries(
        [
            make_bullish_order_block()
        ]
    )

    assert not series.is_empty