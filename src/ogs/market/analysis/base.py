"""
===========================================================

OGS Smart Money AI

Market Analysis Base Classes

===========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class Analyzer(ABC, Generic[T, R]):
    """
    Base class for all market analyzers.
    """

    @abstractmethod
    def analyze(self, data: T) -> R:
        """
        Analyze market data and return a result.
        """
        raise NotImplementedError