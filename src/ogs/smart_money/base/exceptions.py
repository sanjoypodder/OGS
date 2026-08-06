"""
===========================================================

OGS Smart Money AI

Base Exceptions

===========================================================
"""


class SmartMoneyError(Exception):
    """
    Base Smart Money exception.
    """


class ValidationError(SmartMoneyError):
    """
    Validation failure.
    """


class AnalysisError(SmartMoneyError):
    """
    Analysis failure.
    """