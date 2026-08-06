"""
Tests for Watchlist domain.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistStatus,
    WatchlistType,
)


def test_default():

    obj = Watchlist()

    assert obj.watchlist_id == ""
    assert obj.watchlist_name == ""
    assert obj.description == ""
    assert obj.market == ""
    assert obj.owner == ""
    assert obj.symbols == []

    assert obj.watchlist_type == WatchlistType.UNKNOWN
    assert obj.status == WatchlistStatus.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active
    assert obj.symbol_count == 0


def test_valid():

    obj = Watchlist(
        watchlist_id="WL001",
        watchlist_name="Swing Trading",
    )

    assert obj.is_valid


def test_active():

    obj = Watchlist(
        watchlist_id="WL001",
        watchlist_name="Swing Trading",
        status=WatchlistStatus.ACTIVE,
    )

    assert obj.is_active


def test_add_remove_symbol():

    obj = Watchlist()

    obj.add_symbol("RELIANCE")
    obj.add_symbol("TCS")
    obj.add_symbol("RELIANCE")

    assert obj.symbol_count == 2

    obj.remove_symbol("TCS")

    assert obj.symbol_count == 1


def test_to_dict():

    obj = Watchlist()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "watchlist_id" in data
    assert "watchlist_name" in data
    assert "symbols" in data


def test_string():

    obj = Watchlist()

    assert "Watchlist" in str(obj)