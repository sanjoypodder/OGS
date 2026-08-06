"""
===========================================================

OGS Smart Money AI

Currency Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import CurrencyCollection
from .enums import CurrencyType


class CurrencyStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: CurrencyCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def fiat_count(self):

        return len(
            self.collection.fiat()
        )

    @property
    def crypto_count(self):

        return len(
            self.collection.crypto()
        )

    def distribution(self):

        return {
            currency_type.name: sum(
                1
                for currency in self.collection
                if currency.currency_type
                == currency_type
            )
            for currency_type
            in CurrencyType
        }

    def summary(self):

        return {
            "count": self.count,
            "fiat": self.fiat_count,
            "crypto": self.crypto_count,
        }