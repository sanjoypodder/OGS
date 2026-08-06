"""
===========================================================

OGS Smart Money AI

Swing Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.market import CandleSeries

from .collection import SwingSeries


class SwingAnalyzerProtocol(Protocol):
    """
    Swing analyzer interface.
    """

    def analyze(
        self,
        series: CandleSeries,
    ) -> SwingSeries:
        ...