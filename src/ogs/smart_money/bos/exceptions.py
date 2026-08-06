"""
===========================================================

OGS Smart Money AI

Break of Structure Exceptions

===========================================================
"""


class BOSError(Exception):
    """
    Base BOS exception.
    """


class InvalidBOSError(BOSError):
    """
    Raised when a BOS object is invalid.
    """