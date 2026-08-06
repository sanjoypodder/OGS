"""
OGS FinOS

Flip Zone Factory

Factory for creating Flip Zone analyzers.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from ogs.smart_money.flip_zone.analyzer import FlipZoneAnalyzer


class FlipZoneFactory:
    """
    Factory for creating Flip Zone components.
    """

    @staticmethod
    def create_analyzer() -> FlipZoneAnalyzer:
        """
        Create a Flip Zone Analyzer.

        Returns
        -------
        FlipZoneAnalyzer
            Configured analyzer instance.
        """
        return FlipZoneAnalyzer()