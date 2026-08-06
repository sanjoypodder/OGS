"""
===========================================================

OGS Smart Money AI

CHOCH Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.smart_money.bos import BOSSeries

from .collection import CHOCHSeries


class CHOCHAnalyzerProtocol(
    Protocol,
):
    """
    CHOCH analyzer interface.
    """

    def analyze(
        self,
        bos: BOSSeries,
    ) -> CHOCHSeries:
        ...