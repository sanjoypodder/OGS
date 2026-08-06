"""
===========================================================

OGS Smart Money AI

Pair Detector Base Class

===========================================================
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from ogs.smart_money.base import BaseDetector

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class PairDetector(
    BaseDetector[TInput, TOutput],
    Generic[TInput, TOutput],
):
    """
    Base class for detectors that analyze
    adjacent pairs of objects.
    """

    @abstractmethod
    def detect(
        self,
        data: TInput,
    ) -> TOutput:
        ...