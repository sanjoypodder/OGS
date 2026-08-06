"""
Tests for RepositoryAnalyzer detection methods.
"""

from ogs.market_data.repository import (
    RepositoryAnalyzer,
    RepositoryCollection,
    RepositoryFactory,
)


def create_analyzer():

    collection = RepositoryCollection(
        [
            RepositoryFactory.create(
                name="Repo1",
                provider="FYERS",
                records=100,
            ),
            RepositoryFactory.create(
                name="Repo2",
                provider="FYERS",
                records=200,
            ),
            RepositoryFactory.create(
                name="Repo3",
                provider="NSE",
                records=300,
            ),
        ]
    )

    return RepositoryAnalyzer(collection)


def test_storage_analysis():

    analyzer = create_analyzer()

    result = analyzer.storage_analysis()

    assert result["repositories"] == 3
    assert isinstance(result["distribution"], dict)


def test_capacity_analysis():

    analyzer = create_analyzer()

    result = analyzer.capacity_analysis()

    assert result["total_records"] == 600
    assert result["largest_repository"] == "Repo3"
    assert result["smallest_repository"] == "Repo1"


def test_provider_analysis():

    analyzer = create_analyzer()

    providers = analyzer.provider_analysis()

    assert providers["FYERS"] == 2
    assert providers["NSE"] == 1