"""
OGS Smart Money AI

Contract Statistics
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import ContractCollection
from .enums import ContractStatus, ContractType


class ContractStatistics(BaseStatistics):
    """
    Statistics for ContractCollection.
    """

    def __init__(
        self,
        collection: ContractCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def active_count(self):

        return len(self.collection.active())

    @property
    def expired_count(self):

        return len(self.collection.expired())

    @property
    def future_count(self):

        return len(self.collection.futures())

    @property
    def option_count(self):

        return len(self.collection.options())

    @property
    def perpetual_count(self):

        return len(self.collection.perpetuals())

    def distribution(self):

        return {
            t.name: len(
                [
                    c
                    for c in self.collection
                    if c.contract_type == t
                ]
            )
            for t in ContractType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
            "expired": self.expired_count,
            "futures": self.future_count,
            "options": self.option_count,
            "perpetuals": self.perpetual_count,
        }