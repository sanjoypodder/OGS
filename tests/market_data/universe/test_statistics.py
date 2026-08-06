"""
Tests for Universe statistics.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseCollection,
    UniverseStatistics,
    UniverseStatus,
    UniverseType,
)


def make(
    universe_id,
    name,
    universe_type,
    status,
    symbols,
):

    return Universe(
        universe_id=universe_id,
        universe_name=name,
        universe_type=universe_type,
        status=status,
        symbols=symbols,
    )


def build_collection():

    collection = UniverseCollection()

    collection.add(
        make(
            "UNI001",
            "NIFTY50",
            UniverseType.INDEX,
            UniverseStatus.ACTIVE,
            ["RELIANCE", "TCS", "INFY"],
        )
    )

    collection.add(
        make(
            "UNI002",
            "Favorites",
            UniverseType.WATCHLIST,
            UniverseStatus.ACTIVE,
            ["SBIN", "ITC"],
        )
    )

    collection.add(
        make(
            "UNI003",
            "Archive",
            UniverseType.CUSTOM,
            UniverseStatus.INACTIVE,
            [],
        )
    )

    return collection


def test_counts():

    stats = UniverseStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2
    assert stats.total_symbols == 5


def test_distribution():

    stats = UniverseStatistics(
        build_collection()
    )

    distribution = stats.distribution()

    assert distribution["INDEX"] == 1
    assert distribution["WATCHLIST"] == 1
    assert distribution["CUSTOM"] == 1


def test_summary():

    stats = UniverseStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2
    assert summary["symbols"] == 5