"""
Tests for Screener statistics.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerCollection,
    ScreenerStatistics,
    ScreenerStatus,
    ScreenerType,
)


def make(
    screener_id,
    name,
    screener_type,
    status,
    filters,
):

    return Screener(
        screener_id=screener_id,
        screener_name=name,
        screener_type=screener_type,
        status=status,
        filters=filters,
    )


def build_collection():

    collection = ScreenerCollection()

    collection.add(
        make(
            "SCR001",
            "SMC",
            ScreenerType.SMART_MONEY,
            ScreenerStatus.ACTIVE,
            [
                {"field": "volume"},
                {"field": "fvg"},
            ],
        )
    )

    collection.add(
        make(
            "SCR002",
            "AI",
            ScreenerType.AI,
            ScreenerStatus.ACTIVE,
            [
                {"field": "trend"},
            ],
        )
    )

    collection.add(
        make(
            "SCR003",
            "Archived",
            ScreenerType.SYSTEM,
            ScreenerStatus.INACTIVE,
            [],
        )
    )

    return collection


def test_counts():

    stats = ScreenerStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2
    assert stats.total_filters == 3


def test_distribution():

    stats = ScreenerStatistics(
        build_collection()
    )

    distribution = stats.distribution()

    assert distribution["SMART_MONEY"] == 1
    assert distribution["AI"] == 1
    assert distribution["SYSTEM"] == 1


def test_summary():

    stats = ScreenerStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2
    assert summary["filters"] == 3