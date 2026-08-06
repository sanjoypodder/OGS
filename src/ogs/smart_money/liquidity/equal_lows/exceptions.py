"""
===========================================================

OGS Smart Money AI

Equal Low Exceptions

===========================================================
"""


class EqualLowError(Exception):
    """
    Base Equal Low exception.
    """


class InvalidEqualLowError(
    EqualLowError,
):
    """
    Raised when an Equal Low is invalid.
    """