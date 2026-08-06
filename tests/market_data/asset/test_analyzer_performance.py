"""
Performance tests.
"""

from ogs.market_data.asset import (
    Asset,
    AssetAnalyzer,
    AssetCollection,
)


def test_large_collection():

    c = AssetCollection()

    for i in range(1000):

        c.add(
            Asset(
                asset_id=str(i),
                symbol=str(i),
                name=str(i),
            )
        )

    analyzer = AssetAnalyzer(c)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 1000