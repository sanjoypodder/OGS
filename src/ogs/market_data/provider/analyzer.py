"""
OGS Smart Money AI

Provider Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import ProviderCollection
from .statistics import ProviderStatistics


class ProviderAnalyzer(BaseAnalyzer):
    """
    Performs analysis on Provider collections.
    """

    def __init__(self, providers: ProviderCollection):
        self.providers = providers
        self.statistics = ProviderStatistics(providers)

    # ------------------------------------------------------------------
    # Required by BaseAnalyzer
    # ------------------------------------------------------------------

    def analyze(self) -> dict:
        """
        Execute the complete analysis.

        Returns
        -------
        dict
            Complete provider analysis.
        """
        return self.provider_analysis()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> dict:
        return self.statistics.summary()

    # ------------------------------------------------------------------
    # Connection
    # ------------------------------------------------------------------

    def connection_analysis(self) -> dict:
        total = self.statistics.count

        availability = (
            0.0
            if total == 0
            else round(
                self.statistics.connected_count / total * 100,
                2,
            )
        )

        return {
            "total": total,
            "connected": self.statistics.connected_count,
            "offline": self.statistics.offline_count,
            "availability_percent": availability,
        }

    # ------------------------------------------------------------------
    # Latency
    # ------------------------------------------------------------------

    def latency_analysis(self) -> dict:
        fastest = self.statistics.fastest_provider
        slowest = self.statistics.slowest_provider

        return {
            "average_latency_ms": round(
                self.statistics.average_latency,
                2,
            ),
            "fastest_provider": (
                fastest.name if fastest else None
            ),
            "fastest_latency_ms": (
                fastest.latency_ms if fastest else None
            ),
            "slowest_provider": (
                slowest.name if slowest else None
            ),
            "slowest_latency_ms": (
                slowest.latency_ms if slowest else None
            ),
        }

    # ------------------------------------------------------------------
    # Capabilities
    # ------------------------------------------------------------------

    def capability_analysis(self) -> dict:
        return {
            "live_capable": self.statistics.live_capable,
            "historical_capable": (
                self.statistics.historical_capable
            ),
            "websocket_capable": (
                self.statistics.websocket_capable
            ),
            "provider_distribution": (
                self.statistics.provider_distribution
            ),
        }

    # ------------------------------------------------------------------
    # Complete Analysis
    # ------------------------------------------------------------------

    def provider_analysis(self) -> dict:
        return {
            "summary": self.summary(),
            "connection": self.connection_analysis(),
            "latency": self.latency_analysis(),
            "capabilities": self.capability_analysis(),
        }