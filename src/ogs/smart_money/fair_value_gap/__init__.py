"""
===========================================================

OGS Smart Money AI

Fair Value Gap Package

===========================================================
"""

from .analyzer import FairValueGapAnalyzer
from .collection import FairValueGapSeries
from .domain import FairValueGap
from .enums import FairValueGapDirection
from .statistics import FairValueGapStatistics
from .validator import FairValueGapValidator

__all__ = [
    "FairValueGap",
    "FairValueGapDirection",
    "FairValueGapSeries",
    "FairValueGapValidator",
    "FairValueGapStatistics",
    "FairValueGapAnalyzer",
]