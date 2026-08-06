"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Exceptions

===========================================================
"""


class BuySideLiquidityError(Exception):
    """
    Base Buy Side Liquidity exception.
    """


class InvalidBuySideLiquidityError(
    BuySideLiquidityError,
):
    """
    Raised when Buy Side Liquidity is invalid.
    """