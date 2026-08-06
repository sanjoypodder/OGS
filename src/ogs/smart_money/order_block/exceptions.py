"""
===========================================================

OGS Smart Money AI

Order Block Exceptions

===========================================================
"""


class OrderBlockError(Exception):
    """
    Base Order Block exception.
    """


class InvalidOrderBlockError(
    OrderBlockError,
):
    """
    Raised when an Order Block is invalid.
    """