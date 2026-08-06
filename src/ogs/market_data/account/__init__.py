"""
OGS Smart Money AI

Account Module
"""

from .analyzer import AccountAnalyzer
from .collection import AccountCollection
from .domain import Account
from .enums import (
    AccountStatus,
    AccountType,
)
from .factory import AccountFactory
from .statistics import AccountStatistics
from .validator import AccountValidator

__version__ = "0.1.0"

__all__ = [
    "Account",
    "AccountStatus",
    "AccountType",
    "AccountValidator",
    "AccountFactory",
    "AccountCollection",
    "AccountStatistics",
    "AccountAnalyzer",
]