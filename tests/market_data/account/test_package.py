"""
Tests for Account package exports.
"""

from ogs.market_data.account import (
    __version__,
    Account,
    AccountAnalyzer,
    AccountCollection,
    AccountFactory,
    AccountStatistics,
    AccountStatus,
    AccountType,
    AccountValidator,
)


def test_version():
    assert __version__ == "0.1.0"


def test_exports():
    assert Account is not None
    assert AccountAnalyzer is not None
    assert AccountCollection is not None
    assert AccountFactory is not None
    assert AccountStatistics is not None
    assert AccountValidator is not None
    assert AccountStatus is not None
    assert AccountType is not None