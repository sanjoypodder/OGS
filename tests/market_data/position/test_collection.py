"""
Tests for PositionCollection.
"""

from ogs.market_data.position import (
    Position,
    PositionCollection,
    PositionSide,
    PositionStatus,
)


def make_position(
    position_id,
    side=PositionSide.LONG,
    status=PositionStatus.OPEN,
    symbol="NIFTY",
    provider="NSE",
):

    return Position(
        position_id=position_id,
        side=side,
        status=status,
        symbol=symbol,
        provider=provider,
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )


def test_add():

    collection = PositionCollection()

    position = make_position("P1")

    collection.add(position)

    assert len(collection.items) == 1


def test_longs():

    collection = PositionCollection()

    collection.add(make_position("L1", side=PositionSide.LONG))
    collection.add(make_position("S1", side=PositionSide.SHORT))

    assert len(collection.longs()) == 1


def test_shorts():

    collection = PositionCollection()

    collection.add(make_position("L1", side=PositionSide.LONG))
    collection.add(make_position("S1", side=PositionSide.SHORT))

    assert len(collection.shorts()) == 1


def test_open_positions():

    collection = PositionCollection()

    collection.add(make_position("A"))

    collection.add(
        make_position(
            "B",
            status=PositionStatus.CLOSED,
        )
    )

    assert len(collection.open_positions()) == 1


def test_closed_positions():

    collection = PositionCollection()

    collection.add(make_position("A"))

    collection.add(
        make_position(
            "B",
            status=PositionStatus.CLOSED,
        )
    )

    assert len(collection.closed_positions()) == 1


def test_by_symbol():

    collection = PositionCollection()

    collection.add(make_position("A", symbol="AAPL"))
    collection.add(make_position("B", symbol="MSFT"))

    assert len(collection.by_symbol("AAPL")) == 1


def test_by_provider():

    collection = PositionCollection()

    collection.add(make_position("A", provider="NSE"))
    collection.add(make_position("B", provider="BSE"))

    assert len(collection.by_provider("NSE")) == 1


def test_find():

    collection = PositionCollection()

    position = make_position("POS100")

    collection.add(position)

    assert collection.find("POS100") is position


def test_total_market_value():

    collection = PositionCollection()

    collection.add(make_position("A"))
    collection.add(make_position("B"))

    assert collection.total_market_value() == 2200


def test_total_cost_basis():

    collection = PositionCollection()

    collection.add(make_position("A"))
    collection.add(make_position("B"))

    assert collection.total_cost_basis() == 2000


def test_total_realized_pnl():

    collection = PositionCollection()

    p1 = make_position("A")
    p1.realized_pnl = 25

    p2 = make_position("B")
    p2.realized_pnl = 75

    collection.add(p1)
    collection.add(p2)

    assert collection.total_realized_pnl() == 100


def test_total_unrealized_pnl():

    collection = PositionCollection()

    collection.add(make_position("A"))
    collection.add(make_position("B"))

    assert collection.total_unrealized_pnl() == 200


def test_total_pnl():

    collection = PositionCollection()

    p1 = make_position("A")
    p1.realized_pnl = 25

    p2 = make_position("B")
    p2.realized_pnl = 75

    collection.add(p1)
    collection.add(p2)

    assert collection.total_pnl() == 300


def test_to_list():

    collection = PositionCollection()

    collection.add(make_position("A"))

    assert len(collection.to_list()) == 1