"""
Tests for Position domain.
"""

from datetime import UTC
from datetime import datetime

from ogs.market_data.position import (
    Position,
    PositionSide,
    PositionStatus,
)


def test_default_position():

    position = Position()

    assert position.position_id == ""
    assert position.quantity == 0.0
    assert position.average_entry_price == 0.0
    assert position.current_price == 0.0


def test_cost_basis():

    position = Position(
        quantity=10,
        average_entry_price=100,
    )

    assert position.cost_basis == 1000


def test_market_value():

    position = Position(
        quantity=10,
        current_price=120,
    )

    assert position.market_value == 1200


def test_unrealized_pnl_long():

    position = Position(
        side=PositionSide.LONG,
        quantity=10,
        average_entry_price=100,
        current_price=120,
    )

    assert position.unrealized_pnl == 200


def test_unrealized_pnl_short():

    position = Position(
        side=PositionSide.SHORT,
        quantity=10,
        average_entry_price=120,
        current_price=100,
    )

    assert position.unrealized_pnl == 200


def test_total_pnl():

    position = Position(
        side=PositionSide.LONG,
        quantity=10,
        average_entry_price=100,
        current_price=120,
        realized_pnl=50,
    )

    assert position.total_pnl == 250


def test_return_percentage():

    position = Position(
        side=PositionSide.LONG,
        quantity=10,
        average_entry_price=100,
        current_price=120,
    )

    assert position.return_percentage == 20.0


def test_is_long():

    position = Position(side=PositionSide.LONG)

    assert position.is_long


def test_is_short():

    position = Position(side=PositionSide.SHORT)

    assert position.is_short


def test_is_open():

    position = Position(status=PositionStatus.OPEN)

    assert position.is_open


def test_is_closed():

    position = Position(status=PositionStatus.CLOSED)

    assert position.is_closed


def test_valid_position():

    position = Position(
        quantity=1,
        average_entry_price=10,
        current_price=12,
    )

    assert position.is_valid


def test_invalid_position():

    position = Position(
        quantity=-1,
    )

    assert not position.is_valid


def test_to_dict():

    position = Position(position_id="POS001")

    data = position.to_dict()

    assert data["position_id"] == "POS001"


def test_timestamp():

    position = Position()

    assert isinstance(
        position.opened_at,
        datetime,
    )


def test_custom_timestamp():

    ts = datetime.now(UTC)

    position = Position(opened_at=ts)

    assert position.opened_at == ts


def test_string():

    position = Position(position_id="POS001")

    assert "POS001" in str(position)