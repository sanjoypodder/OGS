"""
Edge case tests for RepositoryAnalyzer.
"""

from ogs.market_data.repository import (
    RepositoryAnalyzer,
    RepositoryCollection,
)


def test_empty_collection():

    analyzer = RepositoryAnalyzer(
        RepositoryCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0
    assert result["capacity"]["total_records"] == 0
    assert result["providers"] == {}


def test_empty_storage_analysis():

    analyzer = RepositoryAnalyzer(
        RepositoryCollection()
    )

    storage = analyzer.storage_analysis()

    assert storage["repositories"] == 0
    assert storage["distribution"] == {}


def test_empty_capacity_analysis():

    analyzer = RepositoryAnalyzer(
        RepositoryCollection()
    )

    capacity = analyzer.capacity_analysis()

    assert capacity["largest_repository"] is None
    assert capacity["smallest_repository"] is None