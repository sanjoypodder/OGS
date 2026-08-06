"""
OGS FinOS

Dealing Range Factory

Factory responsible for creating
DealingRangeAnalyzer instances.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from ogs.smart_money.dealing_range.analyzer import (
    DealingRangeAnalyzer,
)


class DealingRangeFactory:
    """
    Factory for DealingRange components.
    """

    @staticmethod
    def create_analyzer() -> DealingRangeAnalyzer:
        """
        Create a DealingRangeAnalyzer.
        """

        return DealingRangeAnalyzer()