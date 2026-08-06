"""
===========================================================

OGS Smart Money AI

Test Swing Factory

Reusable SwingPoint objects.

===========================================================
"""

from __future__ import annotations

from datetime import datetime

from ogs.market_structure import (
    SwingPoint,
    SwingStrength,
    SwingType,
)

from .candle_factory import CandleFactory


class SwingFactory:
    """
    Factory for creating immutable SwingPoint objects.

    Every SwingPoint produced here is valid and can be reused
    throughout all Market Structure tests.
    """

    @staticmethod
    def create(
        *,
        index: int = 0,
        price: float = 100.0,
        swing_type: SwingType = SwingType.HIGH,
        strength: SwingStrength = SwingStrength.NORMAL,
        candle=None,
        symbol: str | None = None,
    ) -> SwingPoint:

        # Only create a default candle if one wasn't supplied.
        if candle is None:
            candle = CandleFactory.btc()

        # IMPORTANT:
        # Preserve an explicitly supplied empty string ("").
        # Only use the candle symbol when symbol is actually None.
        if symbol is None:
            symbol = candle.symbol.value

        return SwingPoint(
            symbol=symbol,
            candle=candle,
            index=index,
            price=price,
            type=swing_type,
            strength=strength,
        )

    # ------------------------------------------------------
    # Basic Swings
    # ------------------------------------------------------

    @staticmethod
    def high() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.HIGH,
            price=105.0,
        )

    @staticmethod
    def low() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.LOW,
            price=95.0,
        )

    # ------------------------------------------------------
    # Classified Swings
    # ------------------------------------------------------

    @staticmethod
    def higher_high() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.HIGHER_HIGH,
            price=110.0,
        )

    @staticmethod
    def higher_low() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.HIGHER_LOW,
            price=100.0,
        )

    @staticmethod
    def lower_high() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.LOWER_HIGH,
            price=102.0,
        )

    @staticmethod
    def lower_low() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.LOWER_LOW,
            price=90.0,
        )

    # ------------------------------------------------------
    # Strength Variants
    # ------------------------------------------------------

    @staticmethod
    def strong_high() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.HIGH,
            strength=SwingStrength.STRONG,
            price=105.0,
        )

    @staticmethod
    def weak_high() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.HIGH,
            strength=SwingStrength.WEAK,
            price=105.0,
        )

    @staticmethod
    def strong_low() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.LOW,
            strength=SwingStrength.STRONG,
            price=95.0,
        )

    @staticmethod
    def weak_low() -> SwingPoint:
        return SwingFactory.create(
            swing_type=SwingType.LOW,
            strength=SwingStrength.WEAK,
            price=95.0,
        )

    # ------------------------------------------------------
    # Sequence
    # ------------------------------------------------------

    @staticmethod
    def sequence() -> list[SwingPoint]:
        """
        Returns a deterministic swing sequence for testing.
        """

        candles = CandleFactory.sequence(6)

        return [
            SwingFactory.create(
                candle=candles[0],
                index=0,
                price=100.0,
                swing_type=SwingType.LOW,
            ),
            SwingFactory.create(
                candle=candles[1],
                index=1,
                price=110.0,
                swing_type=SwingType.HIGH,
            ),
            SwingFactory.create(
                candle=candles[2],
                index=2,
                price=104.0,
                swing_type=SwingType.HIGHER_LOW,
            ),
            SwingFactory.create(
                candle=candles[3],
                index=3,
                price=118.0,
                swing_type=SwingType.HIGHER_HIGH,
            ),
            SwingFactory.create(
                candle=candles[4],
                index=4,
                price=109.0,
                swing_type=SwingType.HIGHER_LOW,
            ),
            SwingFactory.create(
                candle=candles[5],
                index=5,
                price=125.0,
                swing_type=SwingType.HIGHER_HIGH,
            ),
        ]

    # ------------------------------------------------------
    # Timestamp Helper
    # ------------------------------------------------------

    @staticmethod
    def at(
        timestamp: datetime,
        *,
        swing_type: SwingType = SwingType.HIGH,
        price: float = 100.0,
    ) -> SwingPoint:

        candle = CandleFactory.at(timestamp)

        return SwingFactory.create(
            candle=candle,
            swing_type=swing_type,
            price=price,
        ) 