"""
===========================================================

OGS Smart Money AI

Transform Detector Base Class

===========================================================
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from ogs.smart_money.base import BaseDetector

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class TransformDetector(
    BaseDetector[TInput, TOutput],
    Generic[TInput, TOutput],
):
    """
    Base class for detectors that transform
    one domain object into another.
    """

    @abstractmethod
    def detect(
        self,
        data: TInput,
    ) -> TOutput:
        ...