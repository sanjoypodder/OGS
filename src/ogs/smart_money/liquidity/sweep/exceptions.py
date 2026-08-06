"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Exceptions

===========================================================
"""


class LiquiditySweepError(Exception):
    """
    Base Liquidity Sweep exception.
    """


class InvalidLiquiditySweepError(
    LiquiditySweepError,
):
    """
    Raised when a Liquidity Sweep is invalid.
    """