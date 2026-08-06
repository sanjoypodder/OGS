"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Collection Tests

===========================================================
"""

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweepSeries,
)


def test_create_series():

    series = LiquiditySweepSeries([])

    assert len(series) == 0


def test_append(sample_sweep):

    series = LiquiditySweepSeries([])

    series.append(sample_sweep)

    assert len(series) == 1


def test_first(sample_sweep):

    series = LiquiditySweepSeries([sample_sweep])

    assert series.first == sample_sweep


def test_last(sample_sweep):

    series = LiquiditySweepSeries([sample_sweep])

    assert series.last == sample_sweep


def test_latest(sample_sweep):

    series = LiquiditySweepSeries([sample_sweep])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_sweep


def test_is_empty():

    series = LiquiditySweepSeries([])

    assert series.is_empty


def test_not_empty(sample_sweep):

    series = LiquiditySweepSeries([sample_sweep])

    assert not series.is_empty


def test_iteration(sample_sweep):

    series = LiquiditySweepSeries([sample_sweep])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_sweep


def test_indexing(sample_sweep):

    series = LiquiditySweepSeries([sample_sweep])

    assert series[0] == sample_sweep