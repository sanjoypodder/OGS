"""
OGS Framework Package

This package provides the common foundation for all OGS modules.

Modules:
    - analyzer
    - collection
    - exceptions
    - factory
    - interfaces
    - statistics
    - validator
"""

from .analyzer import BaseAnalyzer
from .collection import BaseCollection
from .exceptions import (
    AnalyzerError,
    CollectionError,
    FactoryError,
    OGSException,
    ValidationError,
)
from .factory import BaseFactory
from .interfaces import (
    AnalyzerInterface,
    CollectionInterface,
    FactoryInterface,
    StatisticsInterface,
    ValidatorInterface,
)
from .statistics import BaseStatistics
from .validator import BaseValidator

__version__ = "0.1.0"

__author__ = "OGS Smart Money AI"

__all__ = [
    # Base Classes
    "BaseAnalyzer",
    "BaseCollection",
    "BaseFactory",
    "BaseStatistics",
    "BaseValidator",

    # Interfaces
    "AnalyzerInterface",
    "CollectionInterface",
    "FactoryInterface",
    "StatisticsInterface",
    "ValidatorInterface",

    # Exceptions
    "OGSException",
    "ValidationError",
    "FactoryError",
    "AnalyzerError",
    "CollectionError",
]