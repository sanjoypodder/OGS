"""
OGS Smart Money AI

Market Module
"""

__version__ = "0.1.0"

from .analyzer import MarketAnalyzer
from .collection import MarketCollection
from .domain import Market
from .enums import (
    MarketStatus,
    MarketType,
)
from .factory import MarketFactory
from .statistics import MarketStatistics
from .validator import MarketValidator

__all__ = [
    "__version__",
    "Market",
    "MarketStatus",
    "MarketType",
    "MarketValidator",
    "MarketFactory",
    "MarketCollection",
    "MarketStatistics",
    "MarketAnalyzer",
]