"""
===========================================================

OGS Smart Money AI

SMT Divergence Collection Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergence,
    SMTDivergenceDirection,
    SMTDivergenceSeries,
)


def make_divergence(index: int = 1) -> SMTDivergence:
    return SMTDivergence(
        first_symbol=f"BTC{index}",
        second_symbol=f"ETH{index}",
        first_price=100.0 + index,
        second_price=95.0 + index,
        comparison=SMTComparisonType.HIGH,
        direction=SMTDivergenceDirection.BULLISH,
        timestamp=datetime(2025, 1, 1) + timedelta(minutes=index),
        confidence=SMTConfidence.MEDIUM,
    )


# ==========================================================
# Construction
# ==========================================================


def test_empty_series():

    series = SMTDivergenceSeries()

    assert len(series) == 0


def test_construct_with_items():

    d1 = make_divergence(1)
    d2 = make_divergence(2)

    series = SMTDivergenceSeries([d1, d2])

    assert len(series) == 2


# ==========================================================
# Append
# ==========================================================


def test_append_one():

    series = SMTDivergenceSeries()

    d = make_divergence()

    series.append(d)

    assert len(series) == 1
    assert series[0] == d


def test_append_multiple():

    series = SMTDivergenceSeries()

    d1 = make_divergence(1)
    d2 = make_divergence(2)
    d3 = make_divergence(3)

    series.append(d1)
    series.append(d2)
    series.append(d3)

    assert len(series) == 3


# ==========================================================
# Latest
# ==========================================================


def test_latest_default():

    series = SMTDivergenceSeries()

    d1 = make_divergence(1)
    d2 = make_divergence(2)
    d3 = make_divergence(3)

    series.append(d1)
    series.append(d2)
    series.append(d3)

    latest = series.latest()

    assert latest == [d3]


def test_latest_two():

    series = SMTDivergenceSeries()

    d1 = make_divergence(1)
    d2 = make_divergence(2)
    d3 = make_divergence(3)

    series.append(d1)
    series.append(d2)
    series.append(d3)

    latest = series.latest(2)

    assert latest == [d2, d3]


def test_latest_all():

    series = SMTDivergenceSeries()

    d1 = make_divergence(1)
    d2 = make_divergence(2)
    d3 = make_divergence(3)

    series.append(d1)
    series.append(d2)
    series.append(d3)

    latest = series.latest(10)

    assert latest == [d1, d2, d3]


# ==========================================================
# Iteration
# ==========================================================


def test_iteration():

    d1 = make_divergence(1)
    d2 = make_divergence(2)

    series = SMTDivergenceSeries([d1, d2])

    items = list(series)

    assert items == [d1, d2]


# ==========================================================
# Indexing
# ==========================================================


def test_index_access():

    d1 = make_divergence(1)
    d2 = make_divergence(2)

    series = SMTDivergenceSeries([d1, d2])

    assert series[0] == d1
    assert series[1] == d2


# ==========================================================
# Contains
# ==========================================================


def test_contains():

    d = make_divergence()

    series = SMTDivergenceSeries([d])

    assert d in series


# ==========================================================
# Empty latest
# ==========================================================


def test_latest_empty():

    series = SMTDivergenceSeries()

    assert series.latest() == []