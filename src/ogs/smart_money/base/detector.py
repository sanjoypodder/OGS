"""
===========================================================

OGS Smart Money AI

Base Detector

===========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class BaseDetector(
    ABC,
    Generic[
        InputT,
        OutputT,
    ],
):
    """
    Base class for all pattern detectors.
    """

    @abstractmethod
    def detect(
        self,
        data: InputT,
    ) -> OutputT:
        """
        Detect patterns from input data.
        """
        raise NotImplementedError