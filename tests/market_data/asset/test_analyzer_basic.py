"""
Tests for Asset analyzer.
"""

from ogs.market_data.asset import (
    Asset,
    AssetAnalyzer,
    AssetCollection,
)


def test_analyzer():

    c = AssetCollection()

    c.add(
        Asset(
            asset_id="AAPL",
            symbol="AAPL",
            name="Apple",
        )
    )

    analyzer = AssetAnalyzer(c)

    result = analyzer.analyze()

    assert "summary" in result
    assert "asset_analysis" in result
    assert "distribution_analysis" in result


def test_summary():

    c = AssetCollection()

    c.add(
        Asset(
            asset_id="BTC",
            symbol="BTC",
            name="Bitcoin",
        )
    )

    analyzer = AssetAnalyzer(c)

    assert analyzer.summary()["count"] == 1