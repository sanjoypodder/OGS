"""
===========================================================

OGS Smart Money AI

Order Block Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.engine.analysis import Analysis

from .collection import OrderBlockSeries


class OrderBlockAnalyzerProtocol(
    Protocol,
):

    def analyze(
        self,
        analysis: Analysis,
    ) -> OrderBlockSeries:
        ...