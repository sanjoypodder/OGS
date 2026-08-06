"""
OGS Smart Money AI

Metadata Module
"""

__version__ = "0.1.0"

from .analyzer import MetadataAnalyzer
from .collection import MetadataCollection
from .domain import Metadata
from .enums import (
    MetadataStatus,
    MetadataType,
    MetadataValueType,
)
from .factory import MetadataFactory
from .statistics import MetadataStatistics
from .validator import MetadataValidator

__all__ = [
    "__version__",
    "Metadata",
    "MetadataType",
    "MetadataStatus",
    "MetadataValueType",
    "MetadataValidator",
    "MetadataFactory",
    "MetadataCollection",
    "MetadataStatistics",
    "MetadataAnalyzer",
]