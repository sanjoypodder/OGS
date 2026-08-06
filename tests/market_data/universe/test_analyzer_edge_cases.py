"""
Tests for Universe analyzer edge cases.
"""

from ogs.market_data.universe import (
    UniverseAnalyzer,
    UniverseCollection,
)


def test_empty_collection():

    analyzer = UniverseAnalyzer()

    result = analyzer.analyze(
        UniverseCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = UniverseAnalyzer()

    result = analyzer.analyze(
        UniverseCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["universe_type"]

    assert isinstance(distribution, dict)