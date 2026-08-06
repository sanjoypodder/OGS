"""
===========================================================

OGS Smart Money AI

Currency Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Currency


class CurrencyCollection(
    BaseCollection[Currency],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        currency: Currency,
    ) -> None:

        self._items.append(currency)

    def find(
        self,
        currency_code: str,
    ) -> Currency | None:

        for currency in self._items:

            if (
                currency.currency_code
                == currency_code
            ):
                return currency

        return None

    def fiat(self):

        return [
            currency
            for currency in self._items
            if currency.is_fiat
        ]

    def crypto(self):

        return [
            currency
            for currency in self._items
            if currency.is_crypto
        ]

    def to_list(self):

        return list(self._items)