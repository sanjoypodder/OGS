"""
OGS Smart Money AI

Broker Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Broker
from .enums import BrokerStatus


class BrokerCollection(BaseCollection[Broker]):
    """
    Collection of Broker objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Broker]:
        return self._items

    def add(
        self,
        broker: Broker,
    ) -> None:
        self.append(broker)

    def active(self) -> list[Broker]:
        return [
            broker
            for broker in self
            if broker.status == BrokerStatus.ACTIVE
        ]

    def inactive(self) -> list[Broker]:
        return [
            broker
            for broker in self
            if broker.status == BrokerStatus.INACTIVE
        ]

    def find(
        self,
        broker_id: str,
    ) -> Broker | None:

        return next(
            (
                broker
                for broker in self
                if broker.broker_id == broker_id
            ),
            None,
        )

    def total_accounts(self) -> int:
        return sum(
            broker.account_count
            for broker in self
        )

    def total_equity(self) -> float:
        return sum(
            broker.total_equity
            for broker in self
        )

    def total_cash(self) -> float:
        return sum(
            broker.total_cash
            for broker in self
        )

    def total_buying_power(self) -> float:
        return sum(
            broker.total_buying_power
            for broker in self
        )

    def total_margin_used(self) -> float:
        return sum(
            broker.total_margin_used
            for broker in self
        )

    def to_list(self) -> list[dict]:
        return [
            broker.to_dict()
            for broker in self
        ]