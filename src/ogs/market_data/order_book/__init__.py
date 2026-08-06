"""
OGS Smart Money AI

OrderBook Module
"""

from .domain import OrderBook
from .enums import (
    OrderBookStatus,
    OrderBookType,
)
from .validator import OrderBookValidator
from .factory import OrderBookFactory
from .collection import OrderBookCollection
from .statistics import OrderBookStatistics
from .analyzer import OrderBookAnalyzer

__version__ = "0.1.0"

__all__ = [
    "OrderBook",
    "OrderBookType",
    "OrderBookStatus",
    "OrderBookValidator",
    "OrderBookFactory",
    "OrderBookCollection",
    "OrderBookStatistics",
    "OrderBookAnalyzer",
]