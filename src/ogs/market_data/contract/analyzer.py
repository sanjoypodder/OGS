"""
===========================================================

OGS Smart Money AI

Contract Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import ContractCollection
from .statistics import ContractStatistics


class ContractAnalyzer(
    BaseAnalyzer[
        ContractCollection,
        dict,
    ]
):
    """
    Analyzer for ContractCollection.
    """

    def analyze(
        self,
        data: ContractCollection,
    ) -> dict:
        """
        Analyze Contract collection.
        """

        statistics = ContractStatistics(data)

        return {
            "summary": statistics.summary(),
            "contract_analysis": {
                "total_contracts": statistics.count,
                "active_contracts": statistics.active_count,
                "expired_contracts": statistics.expired_count,
            },
            "distribution_analysis": {
                "contract_type": statistics.distribution(),
            },
        }