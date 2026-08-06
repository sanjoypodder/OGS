"""
OGS Smart Money AI

Asset Module
"""

__version__ = "0.1.0"

from .analyzer import AssetAnalyzer
from .collection import AssetCollection
from .domain import Asset
from .enums import (
    AssetType,
)
from .factory import AssetFactory
from .statistics import AssetStatistics
from .validator import AssetValidator

__all__ = [
    "__version__",
    "Asset",
    "AssetType",
    "AssetValidator",
    "AssetFactory",
    "AssetCollection",
    "AssetStatistics",
    "AssetAnalyzer",
]