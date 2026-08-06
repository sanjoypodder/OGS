"""
Settlement Validator
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Settlement
from .enums import (
    SettlementCycle,
    SettlementMethod,
    SettlementStatus,
    SettlementType,
)


class SettlementValidator(
    BaseValidator[Settlement]
):
    """
    Settlement validator.
    """

    def validate(
        self,
        value: Settlement,
    ) -> None:

        if not value.settlement_id.strip():
            raise ValueError(
                "Invalid settlement id."
            )

        if not value.exchange.strip():
            raise ValueError(
                "Invalid exchange."
            )

        if not value.market.strip():
            raise ValueError(
                "Invalid market."
            )

        if not value.instrument.strip():
            raise ValueError(
                "Invalid instrument."
            )

        if not isinstance(
            value.settlement_cycle,
            SettlementCycle,
        ):
            raise ValueError(
                "Invalid settlement cycle."
            )

        if not isinstance(
            value.settlement_method,
            SettlementMethod,
        ):
            raise ValueError(
                "Invalid settlement method."
            )

        if not isinstance(
            value.settlement_type,
            SettlementType,
        ):
            raise ValueError(
                "Invalid settlement type."
            )

        if not isinstance(
            value.status,
            SettlementStatus,
        ):
            raise ValueError(
                "Invalid settlement status."
            )