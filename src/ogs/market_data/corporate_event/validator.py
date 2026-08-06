"""
CorporateEvent Validator
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import CorporateEvent
from .enums import (
    CorporateEventStatus,
    CorporateEventType,
)


class CorporateEventValidator(
    BaseValidator[CorporateEvent]
):
    """
    Corporate event validator.
    """

    def validate(
        self,
        value: CorporateEvent,
    ) -> None:

        if not value.corporate_event_id.strip():
            raise ValueError(
                "Invalid corporate event id."
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

        if not value.event_name.strip():
            raise ValueError(
                "Invalid event name."
            )

        if not isinstance(
            value.corporate_event_type,
            CorporateEventType,
        ):
            raise ValueError(
                "Invalid corporate event type."
            )

        if not isinstance(
            value.status,
            CorporateEventStatus,
        ):
            raise ValueError(
                "Invalid corporate event status."
            )