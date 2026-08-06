"""
OGS FinOS

OTE Factory

Factory responsible for creating
OTEAnalyzer instances.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from ogs.smart_money.ote.analyzer import (
    OTEAnalyzer,
)


class OTEFactory:
    """
    Factory for OTE components.
    """

    @staticmethod
    def create_analyzer() -> OTEAnalyzer:
        """
        Create an OTEAnalyzer.
        """

        return OTEAnalyzer()