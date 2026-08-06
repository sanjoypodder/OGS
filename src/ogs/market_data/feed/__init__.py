"""
OGS Smart Money AI

Feed Package
"""

from .analyzer import FeedAnalyzer
from .collection import FeedCollection
from .domain import Feed
from .enums import (
    FeedStatus,
    FeedType,
)
from .factory import FeedFactory
from .statistics import FeedStatistics
from .validator import FeedValidator

__version__ = "0.1.0"

__author__ = "OGS Smart Money AI"

__all__ = [
    "Feed",
    "FeedType",
    "FeedStatus",
    "FeedValidator",
    "FeedFactory",
    "FeedCollection",
    "FeedStatistics",
    "FeedAnalyzer",
]