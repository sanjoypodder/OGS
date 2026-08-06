"""
===========================================================

OGS Smart Money AI

Corporate Action Validator

===========================================================
"""

from __future__ import annotations

from datetime import date

from ogs.smart_money.base.validator import BaseValidator

from .domain import CorporateAction
from .enums import (
    CorporateActionStatus,
    CorporateActionType,
)


class CorporateActionValidator(
    BaseValidator[CorporateAction],
):
    """
    Corporate Action Validator.
    """

    def validate(
        self,
        value: CorporateAction,
    ) -> None:

        if not value.action_id.strip():
            raise ValueError("Invalid action_id.")

        if not value.symbol.strip():
            raise ValueError("Invalid symbol.")

        if not value.exchange.strip():
            raise ValueError("Invalid exchange.")

        if not value.market.strip():
            raise ValueError("Invalid market.")

        if not isinstance(
            value.action_type,
            CorporateActionType,
        ):
            raise ValueError(
                "Invalid corporate action type."
            )

        if not isinstance(
            value.status,
            CorporateActionStatus,
        ):
            raise ValueError(
                "Invalid corporate action status."
            )

        for field_name in (
            "announcement_date",
            "record_date",
            "ex_date",
            "effective_date",
        ):

            field_value = getattr(
                value,
                field_name,
            )

            if (
                field_value is not None
                and not isinstance(
                    field_value,
                    date,
                )
            ):
                raise ValueError(
                    f"Invalid {field_name}."
                )

        if value.ratio <= 0:
            raise ValueError(
                "Ratio must be greater than zero."
            )

        if value.cash_amount < 0:
            raise ValueError(
                "Cash amount cannot be negative."
            )

        if not value.currency.strip():
            raise ValueError(
                "Invalid currency."
            )