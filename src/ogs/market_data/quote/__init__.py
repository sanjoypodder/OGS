"""
OGS Smart Money AI

Quote Module
"""

from .analyzer import QuoteAnalyzer
from .collection import QuoteCollection
from .domain import Quote
from .enums import (
    QuoteStatus,
    QuoteType,
)
from .factory import QuoteFactory
from .statistics import QuoteStatistics
from .validator import QuoteValidator

__all__ = [
    "Quote",
    "QuoteType",
    "QuoteStatus",
    "QuoteValidator",
    "QuoteFactory",
    "QuoteCollection",
    "QuoteStatistics",
    "QuoteAnalyzer",
]

__version__ = "0.1.0"