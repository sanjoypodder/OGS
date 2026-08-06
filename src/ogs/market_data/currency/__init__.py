"""
OGS Smart Money AI

Currency Module
"""

__version__ = "0.1.0"

from .analyzer import CurrencyAnalyzer
from .collection import CurrencyCollection
from .domain import Currency
from .enums import (
    CurrencyStatus,
    CurrencyType,
)
from .factory import CurrencyFactory
from .statistics import CurrencyStatistics
from .validator import CurrencyValidator

__all__ = [
    "__version__",
    "Currency",
    "CurrencyType",
    "CurrencyStatus",
    "CurrencyValidator",
    "CurrencyFactory",
    "CurrencyCollection",
    "CurrencyStatistics",
    "CurrencyAnalyzer",
]