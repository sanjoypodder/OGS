"""
Tests for Screener analyzer edge cases.
"""

from ogs.market_data.screener import (
    ScreenerAnalyzer,
    ScreenerCollection,
)


def test_empty_collection():

    analyzer = ScreenerAnalyzer()

    result = analyzer.analyze(
        ScreenerCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = ScreenerAnalyzer()

    result = analyzer.analyze(
        ScreenerCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["screener_type"]

    assert isinstance(distribution, dict)