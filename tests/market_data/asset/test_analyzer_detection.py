"""
Analyzer detection tests.
"""

from ogs.market_data.asset import (
    Asset,
    AssetAnalyzer,
    AssetCollection,
    AssetType,
)


def test_distribution():

    c = AssetCollection()

    c.add(
        Asset(
            asset_id="BTC",
            symbol="BTC",
            name="Bitcoin",
            asset_type=AssetType.CRYPTO,
        )
    )

    analyzer = AssetAnalyzer(c)

    result = analyzer.distribution_analysis()

    assert result["asset_type"]["CRYPTO"] == 1