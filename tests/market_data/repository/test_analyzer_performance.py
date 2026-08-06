"""
Performance-oriented tests for RepositoryAnalyzer.
"""

from ogs.market_data.repository import (
    RepositoryAnalyzer,
    RepositoryCollection,
    RepositoryFactory,
)


def test_large_repository_collection():

    repositories = RepositoryCollection(
        RepositoryFactory.create(
            name=f"Repo{i}",
            provider="FYERS",
            records=i,
        )
        for i in range(1000)
    )

    analyzer = RepositoryAnalyzer(repositories)

    summary = analyzer.summary()

    assert summary["count"] == 1000


def test_provider_analysis_large_dataset():

    repositories = RepositoryCollection(
        RepositoryFactory.create(
            name=f"Repo{i}",
            provider="FYERS" if i % 2 == 0 else "NSE",
            records=i,
        )
        for i in range(1000)
    )

    analyzer = RepositoryAnalyzer(repositories)

    providers = analyzer.provider_analysis()

    assert providers["FYERS"] == 500
    assert providers["NSE"] == 500


def test_capacity_large_dataset():

    repositories = RepositoryCollection(
        RepositoryFactory.create(
            name=f"Repo{i}",
            records=i,
        )
        for i in range(1000)
    )

    analyzer = RepositoryAnalyzer(repositories)

    capacity = analyzer.capacity_analysis()

    assert capacity["total_records"] == sum(range(1000))
    assert capacity["largest_repository"] == "Repo999"
    assert capacity["smallest_repository"] == "Repo0"