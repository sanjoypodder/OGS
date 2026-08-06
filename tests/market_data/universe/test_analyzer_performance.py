"""
Tests for Universe analyzer performance.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseAnalyzer,
    UniverseCollection,
    UniverseStatus,
    UniverseType,
)


def test_large_collection():

    collection = UniverseCollection()

    for i in range(1000):

        collection.add(
            Universe(
                universe_id=f"UNI{i}",
                universe_name=f"Universe {i}",
                universe_type=UniverseType.INDEX,
                status=UniverseStatus.ACTIVE,
                symbols=[
                    "RELIANCE",
                    "TCS",
                    "INFY",
                ],
            )
        )

    analyzer = UniverseAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["universe_analysis"][
            "total_universes"
        ]
        == 1000
    )

    assert (
        result["universe_analysis"][
            "active_universes"
        ]
        == 1000
    )

    assert (
        result["universe_analysis"][
            "total_symbols"
        ]
        == 3000
    )