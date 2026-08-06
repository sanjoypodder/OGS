"""
Package tests for Portfolio module.
"""

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioAnalyzer,
    PortfolioCollection,
    PortfolioFactory,
    PortfolioStatistics,
    PortfolioStatus,
    PortfolioType,
    PortfolioValidator,
)


def test_package_imports():

    assert Portfolio is not None
    assert PortfolioType is not None
    assert PortfolioStatus is not None
    assert PortfolioValidator is not None
    assert PortfolioFactory is not None
    assert PortfolioCollection is not None
    assert PortfolioStatistics is not None
    assert PortfolioAnalyzer is not None


def test_package_version():

    import ogs.market_data.portfolio as module

    assert module.__version__ == "0.1.0"