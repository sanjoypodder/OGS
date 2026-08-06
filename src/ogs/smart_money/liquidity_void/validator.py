"""
Liquidity Void Validator
"""

from .domain import LiquidityVoid


class LiquidityVoidValidator:
    """
    Validates Liquidity Void objects.
    """

    @staticmethod
    def validate(liquidity_void: LiquidityVoid) -> None:
        if liquidity_void.first is None:
            raise ValueError("First candle is required.")

        if liquidity_void.last is None:
            raise ValueError("Last candle is required.")

        if liquidity_void.direction is None:
            raise ValueError("Direction is required.")

        if liquidity_void.top < liquidity_void.bottom:
            raise ValueError("Top price must be greater than or equal to Bottom price.")

        if liquidity_void.size < 0:
            raise ValueError("Size cannot be negative.")

        if liquidity_void.candle_count < 2:
            raise ValueError("Liquidity Void must contain at least two candles.")