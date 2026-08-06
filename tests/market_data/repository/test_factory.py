"""
Tests for RepositoryFactory.
"""

from ogs.market_data.repository import (
    Repository,
    RepositoryFactory,
    RepositoryStatus,
    RepositoryType,
)


def test_create():

    repository = RepositoryFactory.create(
        name="Repo",
        provider="FYERS",
        symbol="NIFTY",
        timeframe="1D",
        repository_type=RepositoryType.DATABASE,
        status=RepositoryStatus.ACTIVE,
        records=100,
    )

    assert isinstance(repository, Repository)
    assert repository.name == "Repo"
    assert repository.provider == "FYERS"
    assert repository.symbol == "NIFTY"
    assert repository.timeframe == "1D"
    assert repository.records == 100


def test_memory():

    repository = RepositoryFactory.memory("Memory Repo")

    assert repository.repository_type == RepositoryType.IN_MEMORY
    assert repository.status == RepositoryStatus.ACTIVE


def test_database():

    repository = RepositoryFactory.database("Database Repo")

    assert repository.repository_type == RepositoryType.DATABASE
    assert repository.status == RepositoryStatus.ACTIVE


def test_archive():

    repository = RepositoryFactory.archive("Archive Repo")

    assert repository.status == RepositoryStatus.ARCHIVED
    assert repository.writable is False


def test_clone():

    repository = RepositoryFactory.create(
        name="Original",
        provider="FYERS",
        symbol="BANKNIFTY",
        timeframe="5m",
        records=500,
    )

    clone = RepositoryFactory.clone(repository)

    assert clone == repository