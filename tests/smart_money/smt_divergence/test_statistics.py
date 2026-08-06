"""
===========================================================

OGS Smart Money AI

SMT Divergence Statistics Tests

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
    SMTDivergenceStatistics,
)


def make_divergence(
    index: int,
    direction: SMTDivergenceDirection,
    confidence: SMTConfidence,
) -> SMTDivergence:

    return SMTDivergence(
        first_symbol=f"BTC{index}",
        second_symbol=f"ETH{index}",
        first_price=100 + index,
        second_price=90 + index,
        comparison=SMTComparisonType.HIGH,
        direction=direction,
        timestamp=datetime(2025, 1, 1) + timedelta(minutes=index),
        confidence=confidence,
    )


def build_series() -> SMTDivergenceSeries:

    return SMTDivergenceSeries(
        [
            make_divergence(
                1,
                SMTDivergenceDirection.BULLISH,
                SMTConfidence.HIGH,
            ),
            make_divergence(
                2,
                SMTDivergenceDirection.BEARISH,
                SMTConfidence.MEDIUM,
            ),
            make_divergence(
                3,
                SMTDivergenceDirection.HIDDEN_BULLISH,
                SMTConfidence.LOW,
            ),
            make_divergence(
                4,
                SMTDivergenceDirection.HIDDEN_BEARISH,
                SMTConfidence.HIGH,
            ),
        ]
    )


# ==========================================================
# Count
# ==========================================================

def test_total_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.count == 4


# ==========================================================
# Direction Counts
# ==========================================================

def test_bullish_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.bullish_count == 1


def test_bearish_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.bearish_count == 1


def test_hidden_bullish_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.hidden_bullish_count == 1


def test_hidden_bearish_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.hidden_bearish_count == 1


# ==========================================================
# Confidence Counts
# ==========================================================

def test_high_confidence_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.high_confidence_count == 2


def test_medium_confidence_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.medium_confidence_count == 1


def test_low_confidence_count():

    stats = SMTDivergenceStatistics(build_series())

    assert stats.low_confidence_count == 1


# ==========================================================
# Latest / Oldest
# ==========================================================

def test_latest():

    series = build_series()

    stats = SMTDivergenceStatistics(series)

    assert stats.latest == series.last


def test_oldest():

    series = build_series()

    stats = SMTDivergenceStatistics(series)

    assert stats.oldest == series.first


# ==========================================================
# Empty Series
# ==========================================================

def test_empty_statistics():

    series = SMTDivergenceSeries()

    stats = SMTDivergenceStatistics(series)

    assert stats.count == 0

    assert stats.bullish_count == 0
    assert stats.bearish_count == 0
    assert stats.hidden_bullish_count == 0
    assert stats.hidden_bearish_count == 0

    assert stats.high_confidence_count == 0
    assert stats.medium_confidence_count == 0
    assert stats.low_confidence_count == 0

    assert stats.latest is None
    assert stats.oldest is None