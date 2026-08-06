"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Collection Tests

===========================================================
"""

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquiditySeries,
)


def test_create_series():

    series = BuySideLiquiditySeries([])

    assert len(series) == 0


def test_append(sample_buy_side):

    series = BuySideLiquiditySeries([])

    series.append(sample_buy_side)

    assert len(series) == 1


def test_first(sample_buy_side):

    series = BuySideLiquiditySeries([sample_buy_side])

    assert series.first == sample_buy_side


def test_last(sample_buy_side):

    series = BuySideLiquiditySeries([sample_buy_side])

    assert series.last == sample_buy_side


def test_latest(sample_buy_side):

    series = BuySideLiquiditySeries([sample_buy_side])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_buy_side


def test_is_empty():

    series = BuySideLiquiditySeries([])

    assert series.is_empty


def test_not_empty(sample_buy_side):

    series = BuySideLiquiditySeries([sample_buy_side])

    assert not series.is_empty


def test_iteration(sample_buy_side):

    series = BuySideLiquiditySeries([sample_buy_side])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_buy_side


def test_indexing(sample_buy_side):

    series = BuySideLiquiditySeries([sample_buy_side])

    assert series[0] == sample_buy_side