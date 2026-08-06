"""
Tests for Index analyzer distribution.
"""

from ogs.market_data.index import (
    Index,
    IndexAnalyzer,
    IndexCollection,
    IndexStatus,
    IndexType,
)


def test_distribution_detection():

    collection = IndexCollection()

    collection.add(
        Index(
            index_code="NIFTY50",
            index_name="NIFTY 50",
            exchange="NSE",
            index_type=IndexType.BROAD_MARKET,
            status=IndexStatus.ACTIVE,
        )
    )

    collection.add(
        Index(
            index_code="NIFTYIT",
            index_name="NIFTY IT",
            exchange="NSE",
            index_type=IndexType.SECTOR,
            status=IndexStatus.ACTIVE,
        )
    )

    analyzer = IndexAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert (
        distribution["index_type"]["BROAD_MARKET"]
        == 1
    )

    assert (
        distribution["index_type"]["SECTOR"]
        == 1
    )