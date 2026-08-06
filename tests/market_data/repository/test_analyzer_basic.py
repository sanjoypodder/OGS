"""
Tests for RepositoryAnalyzer basic functionality.
"""

from ogs.market_data.repository import (
    RepositoryAnalyzer,
    RepositoryCollection,
    RepositoryFactory,
)


def create_analyzer():

    collection = RepositoryCollection(
        [
            RepositoryFactory.memory("Memory"),
            RepositoryFactory.database("Database"),
            RepositoryFactory.archive("Archive"),
        ]
    )

    return RepositoryAnalyzer(collection)


def test_creation():

    analyzer = create_analyzer()

    assert analyzer is not None
    assert analyzer.repositories is not None
    assert analyzer.statistics is not None


def test_summary():

    analyzer = create_analyzer()

    summary = analyzer.summary()

    assert isinstance(summary, dict)
    assert summary["count"] == 3


def test_analyze():

    analyzer = create_analyzer()

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result
    assert "storage" in result
    assert "capacity" in result
    assert "providers" in result