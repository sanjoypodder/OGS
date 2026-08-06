"""
Tests for PortfolioAnalyzer basic functionality.
"""

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioAnalyzer,
    PortfolioCollection,
)


def make_portfolio(portfolio_id):

    return Portfolio(
        portfolio_id=portfolio_id,
        name=f"Portfolio {portfolio_id}",
        cash_balance=1000,
    )


def test_analyzer_creation():

    collection = PortfolioCollection()

    analyzer = PortfolioAnalyzer(collection)

    assert analyzer.collection is collection


def test_summary():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))
    collection.add(make_portfolio("P2"))

    analyzer = PortfolioAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 2


def test_analyze():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.analyze()

    assert "summary" in result
    assert "portfolio_analysis" in result
    assert "distribution_analysis" in result