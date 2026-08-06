"""
OGS Smart Money AI

TradingHours Module
"""

__version__ = "0.1.0"

from .analyzer import TradingHoursAnalyzer
from .collection import TradingHoursCollection
from .domain import TradingHours
from .enums import (
    TradingHoursStatus,
    TradingHoursType,
)
from .factory import TradingHoursFactory
from .statistics import TradingHoursStatistics
from .validator import TradingHoursValidator

__all__ = [
    "__version__",
    "TradingHours",
    "TradingHoursType",
    "TradingHoursStatus",
    "TradingHoursValidator",
    "TradingHoursFactory",
    "TradingHoursCollection",
    "TradingHoursStatistics",
    "TradingHoursAnalyzer",
]