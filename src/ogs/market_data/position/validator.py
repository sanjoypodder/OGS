"""
OGS Smart Money AI

Position Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Position
from .enums import (
    PositionSide,
    PositionStatus,
)


class PositionValidator(BaseValidator):
    """
    Validator for Position objects.
    """

    def validate(
        self,
        position: Position,
    ) -> bool:

        if not isinstance(position, Position):
            raise TypeError(
                "Expected Position."
            )

        if not position.position_id:
            raise ValueError(
                "Position ID cannot be empty."
            )

        if not isinstance(
            position.side,
            PositionSide,
        ):
            raise ValueError(
                "Invalid PositionSide."
            )

        if not isinstance(
            position.status,
            PositionStatus,
        ):
            raise ValueError(
                "Invalid PositionStatus."
            )

        if position.quantity < 0:
            raise ValueError(
                "Quantity cannot be negative."
            )

        if position.average_entry_price < 0:
            raise ValueError(
                "Entry price cannot be negative."
            )

        if position.current_price < 0:
            raise ValueError(
                "Current price cannot be negative."
            )

        if position.realized_pnl < 0:
            raise ValueError(
                "Realized PnL cannot be negative."
            )

        if not isinstance(
            position.opened_at,
            datetime,
        ):
            raise ValueError(
                "Invalid opened_at."
            )

        if (
            position.closed_at is not None
            and not isinstance(
                position.closed_at,
                datetime,
            )
        ):
            raise ValueError(
                "Invalid closed_at."
            )

        return True

    def __call__(
        self,
        position: Position,
    ) -> bool:

        return self.validate(position)