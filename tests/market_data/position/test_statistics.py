"""
Tests for PositionStatistics.
"""

from ogs.market_data.position import (
    Position,
    PositionCollection,
    PositionSide,
    PositionStatistics,
)


def make_position(
    position_id,
    side=PositionSide.LONG,
    provider="NSE",
    symbol="NIFTY",
):

    return Position(
        position_id=position_id,
        side=side,
        quantity=10,
        average_entry_price=100,
        current_price=110,
        provider=provider,
        symbol=symbol,
    )


def test_count():

    collection = PositionCollection()

    collection.add(make_position("A"))

    stats = PositionStatistics(collection)

    assert stats.count == 1


def test_long_short_count():

    collection = PositionCollection()

    collection.add(make_position("A", side=PositionSide.LONG))
    collection.add(make_position("B", side=PositionSide.SHORT))

    stats = PositionStatistics(collection)

    assert stats.long_count == 1
    assert stats.short_count == 1


def test_total_market_value():

    collection = PositionCollection()

    collection.add(make_position("A"))
    collection.add(make_position("B"))

    stats = PositionStatistics(collection)

    assert stats.total_market_value == 2200


def test_total_cost_basis():

    collection = PositionCollection()

    collection.add(make_position("A"))
    collection.add(make_position("B"))

    stats = PositionStatistics(collection)

    assert stats.total_cost_basis == 2000


def test_average_return():

    collection = PositionCollection()

    collection.add(make_position("A"))
    collection.add(make_position("B"))

    stats = PositionStatistics(collection)

    assert stats.average_return == 10.0


def test_provider_distribution():

    collection = PositionCollection()

    collection.add(make_position("A", provider="NSE"))

    stats = PositionStatistics(collection)

    assert stats.provider_distribution["NSE"] == 1


def test_symbol_distribution():

    collection = PositionCollection()

    collection.add(make_position("A", symbol="BANKNIFTY"))

    stats = PositionStatistics(collection)

    assert stats.symbol_distribution["BANKNIFTY"] == 1


def test_summary():

    collection = PositionCollection()

    collection.add(make_position("A"))

    stats = PositionStatistics(collection)

    summary = stats.summary()

    assert summary["count"] == 1


def test_empty_statistics():

    collection = PositionCollection()

    stats = PositionStatistics(collection)

    assert stats.average_return == 0.0