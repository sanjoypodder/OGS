"""
===========================================================

OGS Smart Money AI

Currency Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Currency
from .enums import (
    CurrencyStatus,
    CurrencyType,
)


class CurrencyValidator(
    BaseValidator[Currency],
):
    """
    Currency Validator.
    """

    def validate(
        self,
        value: Currency,
    ) -> None:

        if not value.currency_code.strip():
            raise ValueError(
                "Invalid currency code."
            )

        if value.numeric_code <= 0:
            raise ValueError(
                "Invalid numeric code."
            )

        if not value.name.strip():
            raise ValueError(
                "Invalid currency name."
            )

        if not isinstance(
            value.currency_type,
            CurrencyType,
        ):
            raise ValueError(
                "Invalid currency type."
            )

        if not isinstance(
            value.status,
            CurrencyStatus,
        ):
            raise ValueError(
                "Invalid currency status."
            )

        if value.minor_unit < 0:
            raise ValueError(
                "Invalid minor unit."
            )

        if value.exchange_rate <= 0:
            raise ValueError(
                "Invalid exchange rate."
            )