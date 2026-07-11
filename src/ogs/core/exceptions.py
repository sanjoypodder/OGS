"""
===========================================================

Module:
    exceptions.py

Purpose:
    Custom exceptions used throughout OGS.

Author:
    Om Ganapati Solution

===========================================================
"""


class OGSError(Exception):
    """
    Base exception for OGS.
    """


class ConfigurationError(OGSError):
    """
    Configuration related error.
    """


class EnvironmentError(OGSError):
    """
    Environment validation error.
    """


class EngineError(OGSError):
    """
    Engine execution error.
    """


class DataError(OGSError):
    """
    Invalid market data.
    """


class StrategyError(OGSError):
    """
    Strategy execution error.
    """


class DatabaseError(OGSError):
    """
    Database related error.
    """
