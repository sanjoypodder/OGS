"""
===========================================================

OGS Smart Money AI

Equal Low Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.smart_money.swing import SwingSeries

from .collection import EqualLowSeries


class EqualLowDetectorProtocol(
    Protocol,
):

    def detect(
        self,
        swings: SwingSeries,
    ) -> EqualLowSeries:
        ...