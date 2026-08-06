"""
===========================================================

OGS Smart Money AI

CHOCH Exceptions

===========================================================
"""


class CHOCHError(Exception):
    """
    Base CHOCH exception.
    """


class InvalidCHOCHError(
    CHOCHError,
):
    """
    Raised when a CHOCH is invalid.
    """