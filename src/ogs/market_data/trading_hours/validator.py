"""
TradingHours Validator
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import TradingHours
from .enums import (
    TradingHoursStatus,
    TradingHoursType,
)


class TradingHoursValidator(
    BaseValidator[TradingHours]
):

    def validate(
        self,
        value: TradingHours,
    ) -> None:

        if not value.trading_hours_id.strip():
            raise ValueError("Invalid trading hours id.")

        if not value.exchange.strip():
            raise ValueError("Invalid exchange.")

        if not value.market.strip():
            raise ValueError("Invalid market.")

        if not value.session_name.strip():
            raise ValueError("Invalid session name.")

        if not isinstance(
            value.trading_hours_type,
            TradingHoursType,
        ):
            raise ValueError(
                "Invalid trading hours type."
            )

        if not isinstance(
            value.status,
            TradingHoursStatus,
        ):
            raise ValueError(
                "Invalid trading hours status."
            )