"""
===========================================================

OGS Smart Money AI

Order Block Candidate Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .candidate import OrderBlockCandidate


class OrderBlockCandidateSeries(
    BaseCollection[OrderBlockCandidate]
):
    """
    Collection of Order Block candidates.
    """

    def append(
        self,
        candidate: OrderBlockCandidate,
    ):

        self._items.append(candidate)