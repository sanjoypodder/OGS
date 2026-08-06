"""
OGS Smart Money AI

Position Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Position
from .enums import (
    PositionSide,
    PositionStatus,
)


class PositionCollection(BaseCollection[Position]):
    """
    Collection of Position objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Position]:
        """
        Compatibility property.
        """
        return self._items

    def add(self, position: Position) -> None:
        self.append(position)

    def longs(self) -> list[Position]:
        return [
            position
            for position in self
            if position.side == PositionSide.LONG
        ]

    def shorts(self) -> list[Position]:
        return [
            position
            for position in self
            if position.side == PositionSide.SHORT
        ]

    def open_positions(self) -> list[Position]:
        return [
            position
            for position in self
            if position.status == PositionStatus.OPEN
        ]

    def closed_positions(self) -> list[Position]:
        return [
            position
            for position in self
            if position.status == PositionStatus.CLOSED
        ]

    def by_symbol(
        self,
        symbol: str,
    ) -> list[Position]:

        return [
            position
            for position in self
            if position.symbol == symbol
        ]

    def by_provider(
        self,
        provider: str,
    ) -> list[Position]:

        return [
            position
            for position in self
            if position.provider == provider
        ]

    def find(
        self,
        position_id: str,
    ) -> Position | None:

        return next(
            (
                position
                for position in self
                if position.position_id == position_id
            ),
            None,
        )

    def total_market_value(self) -> float:
        return sum(
            position.market_value
            for position in self
        )

    def total_cost_basis(self) -> float:
        return sum(
            position.cost_basis
            for position in self
        )

    def total_realized_pnl(self) -> float:
        return sum(
            position.realized_pnl
            for position in self
        )

    def total_unrealized_pnl(self) -> float:
        return sum(
            position.unrealized_pnl
            for position in self
        )

    def total_pnl(self) -> float:
        return sum(
            position.total_pnl
            for position in self
        )

    def to_list(self) -> list[dict]:
        return [
            position.to_dict()
            for position in self
        ]