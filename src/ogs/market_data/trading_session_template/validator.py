"""
TradingSessionTemplate Validator
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import TradingSessionTemplate
from .enums import (
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


class TradingSessionTemplateValidator(
    BaseValidator[TradingSessionTemplate]
):
    """
    Trading session template validator.
    """

    def validate(
        self,
        value: TradingSessionTemplate,
    ) -> None:

        if not value.trading_session_template_id.strip():
            raise ValueError(
                "Invalid trading session template id."
            )

        if not value.template_name.strip():
            raise ValueError(
                "Invalid template name."
            )

        if not value.exchange.strip():
            raise ValueError(
                "Invalid exchange."
            )

        if not value.market.strip():
            raise ValueError(
                "Invalid market."
            )

        if not value.timezone.strip():
            raise ValueError(
                "Invalid timezone."
            )

        if not isinstance(
            value.trading_days,
            list,
        ):
            raise ValueError(
                "Trading days must be a list."
            )

        if not isinstance(
            value.session_type,
            TradingSessionTemplateType,
        ):
            raise ValueError(
                "Invalid session type."
            )

        if not isinstance(
            value.status,
            TradingSessionTemplateStatus,
        ):
            raise ValueError(
                "Invalid status."
            )