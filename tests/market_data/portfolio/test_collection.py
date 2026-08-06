"""
Tests for PortfolioCollection.
"""

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioCollection,
    PortfolioStatus,
    PortfolioType,
)


def make_portfolio(
    portfolio_id,
    portfolio_type=PortfolioType.LIVE,
    status=PortfolioStatus.ACTIVE,
):

    return Portfolio(
        portfolio_id=portfolio_id,
        name=f"Portfolio {portfolio_id}",
        portfolio_type=portfolio_type,
        status=status,
        cash_balance=1000,
    )


def test_add():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))

    assert len(collection.items) == 1


def test_active():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))
    collection.add(
        make_portfolio(
            "P2",
            status=PortfolioStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_inactive():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))
    collection.add(
        make_portfolio(
            "P2",
            status=PortfolioStatus.INACTIVE,
        )
    )

    assert len(collection.inactive()) == 1


def test_live():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))
    collection.add(
        make_portfolio(
            "P2",
            portfolio_type=PortfolioType.PAPER,
        )
    )

    assert len(collection.live()) == 1


def test_paper():

    collection = PortfolioCollection()

    collection.add(make_portfolio("P1"))
    collection.add(
        make_portfolio(
            "P2",
            portfolio_type=PortfolioType.PAPER,
        )
    )

    assert len(collection.paper()) == 1


def test_backtest():

    collection = PortfolioCollection()

    collection.add(
        make_portfolio(
            "P1",
            portfolio_type=PortfolioType.BACKTEST,
        )
    )

    assert len(collection.backtest()) == 1


def test_find():

    collection = PortfolioCollection()

    portfolio = make_portfolio("PORT100")

    collection.add(portfolio)

    assert collection.find("PORT100") is portfolio


def test_total_cash():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))
    collection.add(make_portfolio("B"))

    assert collection.total_cash() == 2000


def test_total_equity():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))
    collection.add(make_portfolio("B"))

    assert collection.total_equity() == 2000


def test_to_list():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    assert len(collection.to_list()) == 1