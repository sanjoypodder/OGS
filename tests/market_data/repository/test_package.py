"""
Tests for repository package exports.
"""

from ogs.market_data.repository import (
    Repository,
    RepositoryAnalyzer,
    RepositoryCollection,
    RepositoryFactory,
    RepositoryStatistics,
    RepositoryStatus,
    RepositoryType,
    RepositoryValidator,
)


def test_package_imports():
    assert Repository is not None
    assert RepositoryType is not None
    assert RepositoryStatus is not None
    assert RepositoryValidator is not None
    assert RepositoryFactory is not None
    assert RepositoryCollection is not None
    assert RepositoryStatistics is not None
    assert RepositoryAnalyzer is not None


def test_version_exists():
    import ogs.market_data.repository as repository

    assert hasattr(repository, "__version__")
    assert repository.__version__ == "0.1.0"