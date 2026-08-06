"""
OGS Smart Money AI

Contract Collection
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Contract
from .enums import ContractStatus, ContractType


class ContractCollection(BaseCollection):
    """
    Collection of Contract objects.
    """

    @property
    def items(self):
        return self._items

    def add(self, contract: Contract) -> None:
        self._items.append(contract)

    def find(self, contract_id: str) -> Contract | None:

        for contract in self._items:
            if contract.contract_id == contract_id:
                return contract

        return None

    def active(self):

        return [
            c
            for c in self._items
            if c.status == ContractStatus.ACTIVE
        ]

    def expired(self):

        return [
            c
            for c in self._items
            if c.status == ContractStatus.EXPIRED
        ]

    def futures(self):

        return [
            c
            for c in self._items
            if c.contract_type == ContractType.FUTURE
        ]

    def options(self):

        return [
            c
            for c in self._items
            if c.contract_type == ContractType.OPTION
        ]

    def perpetuals(self):

        return [
            c
            for c in self._items
            if c.contract_type == ContractType.PERPETUAL
        ]

    def to_list(self):

        return list(self._items)