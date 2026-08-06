"""
===========================================================

OGS Smart Money AI

Equal High Package

===========================================================
"""

from .collection import EqualHighSeries
from .detector import EqualHighDetector
from .domain import EqualHigh
from .enums import EqualHighType
from .statistics import EqualHighStatistics
from .validator import EqualHighValidator

__all__ = [
    "EqualHigh",
    "EqualHighType",
    "EqualHighSeries",
    "EqualHighDetector",
    "EqualHighValidator",
    "EqualHighStatistics",
]