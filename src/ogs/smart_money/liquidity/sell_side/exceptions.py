"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Exceptions

===========================================================
"""


class SellSideLiquidityError(Exception):
    """
    Base Sell Side Liquidity exception.
    """


class InvalidSellSideLiquidityError(
    SellSideLiquidityError,
):
    """
    Raised when Sell Side Liquidity is invalid.
    """