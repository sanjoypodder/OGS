"""
===========================================================

OGS Smart Money AI

Corporate Action Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import CorporateActionCollection
from .enums import CorporateActionType


class CorporateActionStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: CorporateActionCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def dividend_count(self):

        return len(
            self.collection.dividends()
        )

    @property
    def effective_count(self):

        return len(
            self.collection.effective()
        )

    def distribution(self):

        return {
            action_type.name: sum(
                1
                for action in self.collection
                if action.action_type
                == action_type
            )
            for action_type
            in CorporateActionType
        }

    def summary(self):

        return {
            "count": self.count,
            "dividends": self.dividend_count,
            "effective": self.effective_count,
        }