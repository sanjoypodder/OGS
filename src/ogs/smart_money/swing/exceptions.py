"""
===========================================================

OGS Smart Money AI

Swing Exceptions

===========================================================
"""


class SwingError(Exception):
    """
    Base Swing exception.
    """


class InvalidSwingError(SwingError):
    """
    Raised when a Swing is invalid.
    """