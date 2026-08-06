"""
===========================================================

OGS Smart Money AI

Smart Money Base Framework

===========================================================
"""

from .analyzer import BaseAnalyzer
from .collection import BaseCollection
from .exceptions import (
    AnalysisError,
    SmartMoneyError,
    ValidationError,
)
from .interfaces import AnalyzerProtocol
from .statistics import BaseStatistics
from .validator import BaseValidator
from .detector import BaseDetector


__all__ = [
    "BaseAnalyzer",
    "BaseCollection",
    "BaseDetector",
    "BaseStatistics",
    "BaseValidator",
    "AnalyzerProtocol",
    "SmartMoneyError",
    "ValidationError",
    "AnalysisError",
]