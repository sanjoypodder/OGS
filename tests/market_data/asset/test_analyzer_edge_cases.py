"""
Edge case tests.
"""

from ogs.market_data.asset import (
    AssetAnalyzer,
    AssetCollection,
)


def test_empty():

    analyzer = AssetAnalyzer(
        AssetCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0
    assert result["distribution_analysis"]["asset_type"] == {}