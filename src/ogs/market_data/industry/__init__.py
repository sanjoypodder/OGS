"""
OGS Smart Money AI

Industry Module
"""

__version__ = "0.1.0"

from .analyzer import IndustryAnalyzer
from .collection import IndustryCollection
from .domain import Industry
from .enums import (
    IndustryStatus,
    IndustryType,
)
from .factory import IndustryFactory
from .statistics import IndustryStatistics
from .validator import IndustryValidator

__all__ = [
    "__version__",
    "Industry",
    "IndustryType",
    "IndustryStatus",
    "IndustryValidator",
    "IndustryFactory",
    "IndustryCollection",
    "IndustryStatistics",
    "IndustryAnalyzer",
]