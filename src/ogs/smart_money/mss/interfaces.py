"""
===========================================================

OGS Smart Money AI

MSS Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.smart_money.choch import CHOCHSeries

from .collection import MSSSeries


class MSSAnalyzerProtocol(
    Protocol,
):

    def analyze(
        self,
        series: CHOCHSeries,
    ) -> MSSSeries:
        ...