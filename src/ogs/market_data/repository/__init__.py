"""
OGS Smart Money AI

Repository Package

This package provides the Repository domain implementation
used throughout the OGS Smart Money AI platform.
"""

from .analyzer import RepositoryAnalyzer
from .collection import RepositoryCollection
from .domain import Repository
from .enums import (
    RepositoryStatus,
    RepositoryType,
)
from .factory import RepositoryFactory
from .statistics import RepositoryStatistics
from .validator import RepositoryValidator

__version__ = "0.1.0"

__author__ = "OGS Smart Money AI"

__all__ = [
    # Domain
    "Repository",

    # Enums
    "RepositoryType",
    "RepositoryStatus",

    # Components
    "RepositoryValidator",
    "RepositoryFactory",
    "RepositoryCollection",
    "RepositoryStatistics",
    "RepositoryAnalyzer",
]