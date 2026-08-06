"""
===========================================================

OGS Smart Money AI

MSS Exceptions

===========================================================
"""


class MSSError(Exception):
    """
    Base MSS exception.
    """


class InvalidMSSError(
    MSSError,
):
    """
    Raised when an MSS is invalid.
    """