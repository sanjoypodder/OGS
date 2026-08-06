"""
OGS Smart Money AI

Sector Module
"""

__version__ = "0.1.0"

from .analyzer import SectorAnalyzer
from .collection import SectorCollection
from .domain import Sector
from .enums import (
    SectorStatus,
    SectorType,
)
from .factory import SectorFactory
from .statistics import SectorStatistics
from .validator import SectorValidator

__all__ = [
    "__version__",
    "Sector",
    "SectorType",
    "SectorStatus",
    "SectorValidator",
    "SectorFactory",
    "SectorCollection",
    "SectorStatistics",
    "SectorAnalyzer",
]