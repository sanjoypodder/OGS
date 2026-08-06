"""
===========================================================

OGS Smart Money AI

Market Structure Package Tests

===========================================================
"""

from ogs.market_structure import (
    MarketStructureAnalyzer,
    SwingPoint,
    SwingSeries,
    SwingPointFactory,
    SwingPointValidator,
    SwingStatistics,
    SwingStrength,
    SwingType,
    TrendDirection,
)


def test_import_market_structure_analyzer():
    """
    Analyzer import.
    """

    assert MarketStructureAnalyzer is not None


def test_import_swing_point():
    """
    SwingPoint import.
    """

    assert SwingPoint is not None


def test_import_swing_series():
    """
    SwingSeries import.
    """

    assert SwingSeries is not None


def test_import_factory():
    """
    Factory import.
    """

    assert SwingPointFactory is not None


def test_import_validator():
    """
    Validator import.
    """

    assert SwingPointValidator is not None


def test_import_statistics():
    """
    Statistics import.
    """

    assert SwingStatistics is not None


def test_import_swing_type():
    """
    SwingType import.
    """

    assert SwingType is not None


def test_import_swing_strength():
    """
    SwingStrength import.
    """

    assert SwingStrength is not None


def test_import_trend_direction():
    """
    TrendDirection import.
    """

    assert TrendDirection is not None


def test_enum_members():

    assert SwingType.HIGH.value == "High"

    assert SwingStrength.NORMAL.value == "Normal"

    assert TrendDirection.BULLISH.value == "Bullish"