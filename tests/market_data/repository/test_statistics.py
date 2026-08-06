"""
Tests for RepositoryStatistics.
"""

from ogs.market_data.repository import (
    RepositoryCollection,
    RepositoryFactory,
    RepositoryStatistics,
)


def create_statistics():

    collection = RepositoryCollection(
        [
            RepositoryFactory.memory("Repo1"),
            RepositoryFactory.database("Repo2"),
            RepositoryFactory.archive("Repo3"),
        ]
    )

    return RepositoryStatistics(collection)


def test_count():

    statistics = create_statistics()

    assert statistics.count == 3


def test_active_count():

    statistics = create_statistics()

    assert statistics.active_count == 2


def test_archived_count():

    statistics = create_statistics()

    assert statistics.archived_count == 1


def test_distribution():

    statistics = create_statistics()

    distribution = statistics.repository_distribution

    assert distribution["IN_MEMORY"] == 1
    assert distribution["DATABASE"] == 1


def test_summary():

    statistics = create_statistics()

    summary = statistics.summary()

    assert summary["count"] == 3
    assert "repository_distribution" in summary