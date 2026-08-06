"""
Edge case tests for PortfolioAnalyzer.
"""

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioAnalyzer,
    PortfolioCollection,
)


def test_empty_collection():

    collection = PortfolioCollection()

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_single_portfolio():

    collection = PortfolioCollection()

    collection.add(
        Portfolio(
            portfolio_id="P1",
            name="Main",
        )
    )

    analyzer = PortfolioAnalyzer(collection)

    assert analyzer.summary()["count"] == 1


def test_zero_equity():

    collection = PortfolioCollection()

    collection.add(
        Portfolio(
            portfolio_id="P1",
            name="Main",
            cash_balance=0,
        )
    )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.portfolio_analysis()

    assert result["total_equity"] == 0


def test_zero_return():

    collection = PortfolioCollection()

    collection.add(
        Portfolio(
            portfolio_id="P1",
            name="Main",
            initial_capital=0,
        )
    )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.portfolio_analysis()

    assert result["average_return"] == 0.0