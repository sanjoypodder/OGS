"""
OGS Smart Money AI

Contract Module
"""

__version__ = "0.1.0"

from .analyzer import ContractAnalyzer
from .collection import ContractCollection
from .domain import Contract
from .enums import (
    ContractStatus,
    ContractType,
    ExerciseStyle,
    OptionType,
    SettlementType,
)
from .factory import ContractFactory
from .statistics import ContractStatistics
from .validator import ContractValidator

__all__ = [
    "__version__",
    "Contract",
    "ContractType",
    "OptionType",
    "SettlementType",
    "ExerciseStyle",
    "ContractStatus",
    "ContractValidator",
    "ContractFactory",
    "ContractCollection",
    "ContractStatistics",
    "ContractAnalyzer",
]