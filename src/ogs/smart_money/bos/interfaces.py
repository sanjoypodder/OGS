"""
===========================================================

OGS Smart Money AI

Break of Structure Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.market import CandleSeries

from .collection import BOSSeries


class BOSAnalyzerProtocol(Protocol):
    """
    BOS analyzer interface.
    """

    def analyze(
        self,
        series: CandleSeries,
    ) -> BOSSeries:
        ...