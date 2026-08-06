"""
OGS Smart Money AI

Index Module
"""

__version__ = "0.1.0"

from .analyzer import IndexAnalyzer
from .collection import IndexCollection
from .domain import Index
from .enums import (
    IndexStatus,
    IndexType,
)
from .factory import IndexFactory
from .statistics import IndexStatistics
from .validator import IndexValidator

__all__ = [
    "__version__",
    "Index",
    "IndexType",
    "IndexStatus",
    "IndexValidator",
    "IndexFactory",
    "IndexCollection",
    "IndexStatistics",
    "IndexAnalyzer",
]