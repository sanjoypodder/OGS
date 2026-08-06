"""
===========================================================

OGS Smart Money AI

Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class AnalyzerProtocol(
    Protocol[T, R],
):
    """
    Analyzer interface.
    """

    def analyze(
        self,
        data: T,
    ) -> R:
        ...