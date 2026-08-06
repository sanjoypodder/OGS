"""
===========================================================

OGS Smart Money AI

Order Block Candidate Builder

===========================================================
"""

from __future__ import annotations

from .candidate import OrderBlockCandidate
from ogs.smart_money.candidate import CandidateStatus


class OrderBlockCandidateBuilder:
    """
    Builds Order Block candidates.
    """

    def build(
        self,
        *,
        origin_candle,
        mss,
        liquidity_sweep,
    ) -> OrderBlockCandidate:

        return OrderBlockCandidate(
        status=CandidateStatus.DETECTED,
        origin_candle=origin_candle,
        mss=mss,
        liquidity_sweep=liquidity_sweep,
    )