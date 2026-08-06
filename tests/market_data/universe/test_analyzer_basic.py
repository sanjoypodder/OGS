"""
Tests for Universe analyzer.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseAnalyzer,
    UniverseCollection,
    UniverseStatus,
    UniverseType,
)


def test_analyze():

    collection = UniverseCollection()

    collection.add(
        Universe(
            universe_id="UNI001",
            universe_name="NIFTY50",
            universe_type=UniverseType.INDEX,
            status=UniverseStatus.ACTIVE,
            symbols=["RELIANCE", "TCS"],
        )
    )

    analyzer = UniverseAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "universe_analysis" in result
    assert "distribution_analysis" in result