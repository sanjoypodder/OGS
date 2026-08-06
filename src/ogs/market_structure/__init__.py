"""
===========================================================

OGS Smart Money AI

Market Structure Module

===========================================================
"""

from .analyzer import MarketStructureAnalyzer
from .collection import SwingSeries
from .domain import SwingPoint
from .enums import (
    SwingStrength,
    SwingType,
    TrendDirection,
)
from .factory import SwingPointFactory
from .statistics import SwingStatistics
from .validator import SwingPointValidator

__all__ = [
    "MarketStructureAnalyzer",
    "SwingSeries",
    "SwingPoint",
    "SwingPointFactory",
    "SwingPointValidator",
    "SwingStatistics",
    "SwingType",
    "SwingStrength",
    "TrendDirection",
]