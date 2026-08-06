"""
===========================================================

OGS Smart Money AI

Base Analyzer

===========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class BaseAnalyzer(
    ABC,
    Generic[TInput, TOutput],
):
    """
    Base class for all Smart Money analyzers.
    """

    @abstractmethod
    def analyze(
        self,
        data: TInput,
    ) -> TOutput:
        """
        Analyze input data.
        """
        raise NotImplementedError