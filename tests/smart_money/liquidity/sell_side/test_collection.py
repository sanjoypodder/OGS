"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Collection Tests

===========================================================
"""

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquiditySeries,
)


def test_create_series():

    series = SellSideLiquiditySeries([])

    assert len(series) == 0


def test_append(sample_sell_side):

    series = SellSideLiquiditySeries([])

    series.append(sample_sell_side)

    assert len(series) == 1


def test_first(sample_sell_side):

    series = SellSideLiquiditySeries([sample_sell_side])

    assert series.first == sample_sell_side


def test_last(sample_sell_side):

    series = SellSideLiquiditySeries([sample_sell_side])

    assert series.last == sample_sell_side


def test_latest(sample_sell_side):

    series = SellSideLiquiditySeries([sample_sell_side])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_sell_side


def test_is_empty():

    series = SellSideLiquiditySeries([])

    assert series.is_empty


def test_not_empty(sample_sell_side):

    series = SellSideLiquiditySeries([sample_sell_side])

    assert not series.is_empty


def test_iteration(sample_sell_side):

    series = SellSideLiquiditySeries([sample_sell_side])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_sell_side


def test_indexing(sample_sell_side):

    series = SellSideLiquiditySeries([sample_sell_side])

    assert series[0] == sample_sell_side