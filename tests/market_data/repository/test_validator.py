"""
Tests for Repository domain.
"""

from ogs.market_data.repository import (
    Repository,
    RepositoryStatus,
    RepositoryType,
)


def test_repository_creation():

    repository = Repository(
        name="Historical Data",
        provider="FYERS",
        symbol="NIFTY50",
        timeframe="1D",
        repository_type=RepositoryType.DATABASE,
        status=RepositoryStatus.ACTIVE,
        records=1000,
    )

    assert repository.name == "Historical Data"
    assert repository.provider == "FYERS"
    assert repository.symbol == "NIFTY50"
    assert repository.timeframe == "1D"
    assert repository.repository_type == RepositoryType.DATABASE
    assert repository.status == RepositoryStatus.ACTIVE
    assert repository.records == 1000


def test_active_property():

    repository = Repository(
        name="Repo",
        status=RepositoryStatus.ACTIVE,
    )

    assert repository.active is True
    assert repository.archived is False
    assert repository.read_only is False


def test_archived_property():

    repository = Repository(
        name="Repo",
        status=RepositoryStatus.ARCHIVED,
    )

    assert repository.archived is True


def test_read_only_property():

    repository = Repository(
        name="Repo",
        status=RepositoryStatus.READ_ONLY,
    )

    assert repository.read_only is True


def test_is_valid():

    repository = Repository(name="Repo")

    assert repository.is_valid is True


def test_to_dict():

    repository = Repository(name="Repo")

    data = repository.to_dict()

    assert isinstance(data, dict)
    assert data["name"] == "Repo"


def test_string_representation():

    repository = Repository(name="Repo")

    assert "Repo" in str(repository)


def test_repr():

    repository = Repository(name="Repo")

    assert "Repository(" in repr(repository)