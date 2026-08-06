"""
Tests for Universe factory.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseFactory,
    UniverseStatus,
    UniverseType,
)


def test_create():

    obj = UniverseFactory.create(
        "UNI001",
        "Universe",
    )

    assert isinstance(obj, Universe)


def test_exchange():

    obj = UniverseFactory.exchange(
        "UNI001",
        "NSE",
    )

    assert obj.universe_type == UniverseType.EXCHANGE
    assert obj.status == UniverseStatus.ACTIVE


def test_index():

    obj = UniverseFactory.index(
        "UNI002",
        "NIFTY50",
    )

    assert obj.universe_type == UniverseType.INDEX
    assert obj.status == UniverseStatus.ACTIVE


def test_watchlist():

    obj = UniverseFactory.watchlist(
        "UNI003",
        "Favorites",
    )

    assert obj.universe_type == UniverseType.WATCHLIST


def test_screener():

    obj = UniverseFactory.screener(
        "UNI004",
        "Breakout",
    )

    assert obj.universe_type == UniverseType.SCREENER


def test_portfolio():

    obj = UniverseFactory.portfolio(
        "UNI005",
        "Long Term",
    )

    assert obj.universe_type == UniverseType.PORTFOLIO


def test_ai():

    obj = UniverseFactory.ai(
        "UNI006",
        "AI Universe",
    )

    assert obj.universe_type == UniverseType.AI


def test_clone():

    obj = UniverseFactory.create(
        "UNI001",
        "Universe",
    )

    clone = UniverseFactory.clone(obj)

    assert clone == obj
    assert clone is not obj