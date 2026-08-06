"""
Performance tests for PortfolioAnalyzer.
"""

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioAnalyzer,
    PortfolioCollection,
)


def test_large_collection():

    collection = PortfolioCollection()

    for i in range(1000):

        collection.add(
            Portfolio(
                portfolio_id=f"P{i}",
                name=f"Portfolio {i}",
                cash_balance=1000,
            )
        )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.summary()

    assert result["count"] == 1000


def test_large_analysis():

    collection = PortfolioCollection()

    for i in range(500):

        collection.add(
            Portfolio(
                portfolio_id=f"P{i}",
                name=f"Portfolio {i}",
                cash_balance=1000,
            )
        )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500
    assert result["portfolio_analysis"]["total_cash"] == 500000
    assert result["portfolio_analysis"]["total_equity"] == 500000