"""
===========================================================

OGS Smart Money AI

Equal High Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.smart_money.swing import SwingSeries

from .collection import EqualHighSeries


class EqualHighDetectorProtocol(
    Protocol,
):

    def detect(
        self,
        swings: SwingSeries,
    ) -> EqualHighSeries:
        ...