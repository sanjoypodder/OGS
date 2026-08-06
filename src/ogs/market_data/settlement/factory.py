"""
Settlement Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Settlement
from .enums import (
    SettlementStatus,
    SettlementType,
)


class SettlementFactory:
    """
    Settlement factory.
    """

    @staticmethod
    def create(**kwargs):

        return Settlement(**kwargs)

    @staticmethod
    def cash(**kwargs):

        return Settlement(
            settlement_type=SettlementType.CASH,
            status=SettlementStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def physical(**kwargs):

        return Settlement(
            settlement_type=SettlementType.PHYSICAL,
            status=SettlementStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def net(**kwargs):

        return Settlement(
            settlement_type=SettlementType.NET,
            status=SettlementStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def gross(**kwargs):

        return Settlement(
            settlement_type=SettlementType.GROSS,
            status=SettlementStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def delivery(**kwargs):

        return Settlement(
            settlement_type=SettlementType.DELIVERY,
            status=SettlementStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def custom(**kwargs):

        return Settlement(
            settlement_type=SettlementType.CUSTOM,
            status=SettlementStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        settlement: Settlement,
    ) -> Settlement:

        return deepcopy(settlement)