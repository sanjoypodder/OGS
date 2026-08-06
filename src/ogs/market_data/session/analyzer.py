"""
===========================================================

OGS Smart Money AI

Session Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import SessionCollection
from .statistics import SessionStatistics


class SessionAnalyzer(
    BaseAnalyzer[
        SessionCollection,
        dict,
    ]
):
    """
    Session Analyzer.
    """

    def analyze(
        self,
        data: SessionCollection,
    ) -> dict:

        statistics = SessionStatistics(data)

        return {
            "summary": statistics.summary(),
            "session_analysis": {
                "total_sessions": statistics.count,
                "active_sessions": statistics.active_count,
                "closed_sessions": statistics.closed_count,
            },
            "distribution_analysis": {
                "session_type": statistics.distribution(),
            },
        }