"""
Tests for PositionValidator.
"""

from datetime import UTC
from datetime import datetime

import pytest

from ogs.market_data.position import (
    Position,
    PositionSide,
    PositionStatus,
    PositionValidator,
)


validator = PositionValidator()


def test_validator_accepts_valid_position():

    position = Position(
        position_id="POS001",
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )

    assert validator(position)


def test_validator_rejects_non_position():

    with pytest.raises(TypeError):
        validator("invalid")


def test_validator_rejects_empty_position_id():

    with pytest.raises(ValueError):
        validator(Position())


def test_negative_quantity():

    with pytest.raises(ValueError):
        validator(
            Position(
                position_id="POS001",
                quantity=-1,
            )
        )


def test_negative_entry_price():

    with pytest.raises(ValueError):
        validator(
            Position(
                position_id="POS001",
                average_entry_price=-1,
            )
        )


def test_negative_current_price():

    with pytest.raises(ValueError):
        validator(
            Position(
                position_id="POS001",
                current_price=-1,
            )
        )


def test_invalid_side():

    position = Position(position_id="POS001")

    position.side = "LONG"

    with pytest.raises(ValueError):
        validator(position)


def test_invalid_status():

    position = Position(position_id="POS001")

    position.status = "OPEN"

    with pytest.raises(ValueError):
        validator(position)


def test_invalid_opened_at():

    position = Position(position_id="POS001")

    position.opened_at = "today"

    with pytest.raises(ValueError):
        validator(position)


def test_invalid_closed_at():

    position = Position(position_id="POS001")

    position.closed_at = "tomorrow"

    with pytest.raises(ValueError):
        validator(position)


def test_callable_validator():

    position = Position(
        position_id="POS001",
        quantity=10,
    )

    assert validator(position)


def test_valid_enums():

    assert isinstance(
        PositionSide.LONG,
        PositionSide,
    )

    assert isinstance(
        PositionStatus.OPEN,
        PositionStatus,
    )


def test_valid_datetime():

    assert isinstance(
        datetime.now(UTC),
        datetime,
    )