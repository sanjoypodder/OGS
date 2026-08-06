"""
OGS Smart Money AI
------------------

SMT Divergence Enums

Defines the supported Smart Money Technique (SMT) divergence
types detected between two correlated markets.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from enum import Enum


class SMTDivergenceDirection(str, Enum):
    """
    Supported SMT Divergence directions.
    """

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    HIDDEN_BULLISH = "Hidden Bullish"
    HIDDEN_BEARISH = "Hidden Bearish"


class SMTComparisonType(str, Enum):
    """
    Price component used for comparison.
    """

    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"


class SMTConfidence(str, Enum):
    """
    Confidence level assigned to an SMT divergence.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"