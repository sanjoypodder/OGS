"""
===========================================================

OGS Smart Money AI

Market Structure Factory

===========================================================
"""

from ogs.market import Candle

from .domain import SwingPoint
from .enums import (
    SwingStrength,
    SwingType,
)
from .validator import SwingPointValidator


class SwingPointFactory:
    """
    Factory for creating validated SwingPoint objects.
    """

    _validator = SwingPointValidator()

    @classmethod
    def create(
        cls,
        *,
        symbol: str,
        candle: Candle,
        index: int,
        price: float,
        type: SwingType,
        strength: SwingStrength = SwingStrength.NORMAL,
    ) -> SwingPoint:
        """
        Create a validated SwingPoint.

        Returns
        -------
        SwingPoint
        """

        swing = SwingPoint(
            symbol=symbol,
            candle=candle,
            index=index,
            price=price,
            type=type,
            strength=strength,
        )

        if not cls._validator.validate(swing):
            raise ValueError(
                "Invalid SwingPoint."
            )

        return swing