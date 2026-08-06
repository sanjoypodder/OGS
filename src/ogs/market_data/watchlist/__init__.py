"""
OGS Smart Money AI

Watchlist Module
"""

__version__ = "0.1.0"

from .analyzer import WatchlistAnalyzer
from .collection import WatchlistCollection
from .domain import Watchlist
from .enums import (
    WatchlistStatus,
    WatchlistType,
)
from .factory import WatchlistFactory
from .statistics import WatchlistStatistics
from .validator import WatchlistValidator

__all__ = [
    "__version__",
    "Watchlist",
    "WatchlistType",
    "WatchlistStatus",
    "WatchlistValidator",
    "WatchlistFactory",
    "WatchlistCollection",
    "WatchlistStatistics",
    "WatchlistAnalyzer",
]