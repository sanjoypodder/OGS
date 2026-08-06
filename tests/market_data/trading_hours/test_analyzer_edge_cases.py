"""
Tests for TradingHours analyzer edge cases.
"""

from ogs.market_data.trading_hours import (
    TradingHoursAnalyzer,
    TradingHoursCollection,
)


def test_empty_collection():

    analyzer = TradingHoursAnalyzer()

    result = analyzer.analyze(
        TradingHoursCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = TradingHoursAnalyzer()

    result = analyzer.analyze(
        TradingHoursCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]

    assert isinstance(
        distribution["trading_hours_type"],
        dict,
    )