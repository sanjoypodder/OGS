"""
Tests for PositionFactory.
"""

import pytest

from ogs.market_data.position import (
    Position,
    PositionFactory,
    PositionSide,
    PositionStatus,
)


def test_create():

    position = PositionFactory.create(
        position_id="POS001",
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )

    assert isinstance(position, Position)


def test_long_factory():

    position = PositionFactory.long(
        position_id="LONG001",
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )

    assert position.side == PositionSide.LONG
    assert position.status == PositionStatus.OPEN


def test_short_factory():

    position = PositionFactory.short(
        position_id="SHORT001",
        quantity=10,
        average_entry_price=100,
        current_price=90,
    )

    assert position.side == PositionSide.SHORT
    assert position.status == PositionStatus.OPEN


def test_clone():

    position = PositionFactory.create(
        position_id="POS001",
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )

    clone = PositionFactory.clone(position)

    assert clone == position
    assert clone is not position


def test_clone_independent():

    position = PositionFactory.create(
        position_id="POS001",
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )

    clone = PositionFactory.clone(position)

    clone.current_price = 150

    assert position.current_price == 110


def test_factory_validation():

    with pytest.raises(ValueError):

        PositionFactory.create(
            position_id="",
            quantity=10,
        )


def test_factory_negative_quantity():

    with pytest.raises(ValueError):

        PositionFactory.create(
            position_id="POS001",
            quantity=-1,
        )