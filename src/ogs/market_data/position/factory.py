"""
OGS Smart Money AI

Position Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Position
from .enums import (
    PositionSide,
    PositionStatus,
)
from .validator import PositionValidator


class PositionFactory(BaseFactory):
    """
    Factory for Position objects.
    """

    validator = PositionValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Position:

        position = Position(**kwargs)

        cls.validator(position)

        return position

    @classmethod
    def long(
        cls,
        **kwargs,
    ) -> Position:

        kwargs["side"] = PositionSide.LONG
        kwargs.setdefault(
            "status",
            PositionStatus.OPEN,
        )

        return cls.create(**kwargs)

    @classmethod
    def short(
        cls,
        **kwargs,
    ) -> Position:

        kwargs["side"] = PositionSide.SHORT
        kwargs.setdefault(
            "status",
            PositionStatus.OPEN,
        )

        return cls.create(**kwargs)

    @classmethod
    def clone(
        cls,
        position: Position,
    ) -> Position:

        clone = deepcopy(position)

        cls.validator(clone)

        return clone