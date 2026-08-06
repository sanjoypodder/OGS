"""
Detection tests for PortfolioAnalyzer.
"""

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioAnalyzer,
    PortfolioCollection,
    PortfolioStatus,
    PortfolioType,
)


def test_portfolio_analysis():

    collection = PortfolioCollection()

    collection.add(
        Portfolio(
            portfolio_id="LIVE1",
            name="Live",
            portfolio_type=PortfolioType.LIVE,
            status=PortfolioStatus.ACTIVE,
            cash_balance=1000,
        )
    )

    collection.add(
        Portfolio(
            portfolio_id="PAPER1",
            name="Paper",
            portfolio_type=PortfolioType.PAPER,
            status=PortfolioStatus.INACTIVE,
            cash_balance=500,
        )
    )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.portfolio_analysis()

    assert result["active_count"] == 1
    assert result["inactive_count"] == 1
    assert result["live_count"] == 1
    assert result["paper_count"] == 1


def test_distribution_analysis():

    collection = PortfolioCollection()

    collection.add(
        Portfolio(
            portfolio_id="P1",
            name="Main",
            portfolio_type=PortfolioType.LIVE,
            status=PortfolioStatus.ACTIVE,
        )
    )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert "status" in result
    assert "types" in result


def test_total_cash_detection():

    collection = PortfolioCollection()

    collection.add(
        Portfolio(
            portfolio_id="P1",
            name="Main",
            cash_balance=2000,
        )
    )

    analyzer = PortfolioAnalyzer(collection)

    result = analyzer.portfolio_analysis()

    assert result["total_cash"] == 2000