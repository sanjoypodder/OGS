"""
===========================================================

OGS Smart Money AI

Equal High Exceptions

===========================================================
"""


class EqualHighError(Exception):
    """
    Base Equal High exception.
    """


class InvalidEqualHighError(
    EqualHighError,
):
    """
    Raised when Equal High is invalid.
    """