"""
Tests for Index statistics.
"""

from ogs.market_data.index import (
    Index,
    IndexCollection,
    IndexStatistics,
    IndexStatus,
    IndexType,
)


def make(code, name, index_type, status):

    return Index(
        index_code=code,
        index_name=name,
        exchange="NSE",
        index_type=index_type,
        status=status,
    )


def build_collection():

    collection = IndexCollection()

    collection.add(
        make(
            "NIFTY50",
            "NIFTY 50",
            IndexType.BROAD_MARKET,
            IndexStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "NIFTYIT",
            "NIFTY IT",
            IndexType.SECTOR,
            IndexStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "OLD",
            "Old Index",
            IndexType.SECTOR,
            IndexStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = IndexStatistics(build_collection())

    assert stats.count == 3
    assert stats.active_count == 2


def test_distribution():

    stats = IndexStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["BROAD_MARKET"] == 1
    assert distribution["SECTOR"] == 2


def test_summary():

    stats = IndexStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2