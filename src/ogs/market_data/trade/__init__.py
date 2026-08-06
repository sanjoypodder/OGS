"""
OGS Smart Money AI

Trade Module
"""

from .analyzer import TradeAnalyzer
from .collection import TradeCollection
from .domain import Trade
from .enums import (
    TradeSide,
    TradeStatus,
)
from .factory import TradeFactory
from .statistics import TradeStatistics
from .validator import TradeValidator

__version__ = "0.1.0"

__all__ = [
    "Trade",
    "TradeSide",
    "TradeStatus",
    "TradeValidator",
    "TradeFactory",
    "TradeCollection",
    "TradeStatistics",
    "TradeAnalyzer",
]