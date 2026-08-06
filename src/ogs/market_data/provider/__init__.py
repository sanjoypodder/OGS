"""
OGS Smart Money AI

Provider Package

This package provides the Provider domain implementation used
throughout the OGS Smart Money AI platform.

Modules
-------
- enums
- domain
- validator
- factory
- collection
- statistics
- analyzer
"""

from .analyzer import ProviderAnalyzer
from .collection import ProviderCollection
from .domain import Provider
from .enums import (
    ConnectionStatus,
    ProviderType,
)
from .factory import ProviderFactory
from .statistics import ProviderStatistics
from .validator import ProviderValidator

__version__ = "0.1.0"

__author__ = "OGS Smart Money AI"

__all__ = [
    # Domain
    "Provider",

    # Enums
    "ProviderType",
    "ConnectionStatus",

    # Components
    "ProviderValidator",
    "ProviderFactory",
    "ProviderCollection",
    "ProviderStatistics",
    "ProviderAnalyzer",
]