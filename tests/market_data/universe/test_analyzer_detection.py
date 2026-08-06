"""
Tests for Universe analyzer distribution.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseAnalyzer,
    UniverseCollection,
    UniverseStatus,
    UniverseType,
)


def test_distribution_detection():

    collection = UniverseCollection()

    collection.add(
        Universe(
            universe_id="UNI001",
            universe_name="NIFTY50",
            universe_type=UniverseType.INDEX,
            status=UniverseStatus.ACTIVE,
        )
    )

    collection.add(
        Universe(
            universe_id="UNI002",
            universe_name="Favorites",
            universe_type=UniverseType.WATCHLIST,
            status=UniverseStatus.ACTIVE,
        )
    )

    analyzer = UniverseAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result[
        "distribution_analysis"
    ]

    assert (
        distribution["universe_type"]["INDEX"]
        == 1
    )

    assert (
        distribution["universe_type"]["WATCHLIST"]
        == 1
    )