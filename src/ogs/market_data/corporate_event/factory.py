"""
CorporateEvent Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import CorporateEvent
from .enums import (
    CorporateEventStatus,
    CorporateEventType,
)


class CorporateEventFactory:
    """
    Corporate event factory.
    """

    @staticmethod
    def create(**kwargs):

        return CorporateEvent(**kwargs)

    @staticmethod
    def earnings(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.EARNINGS,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def dividend(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.DIVIDEND,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def stock_split(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.STOCK_SPLIT,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def bonus(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.BONUS,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def rights(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.RIGHTS,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def merger(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.MERGER,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def acquisition(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.ACQUISITION,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def ipo(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.IPO,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def buyback(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.BUYBACK,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def custom(**kwargs):

        return CorporateEvent(
            corporate_event_type=CorporateEventType.CUSTOM,
            status=CorporateEventStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        corporate_event: CorporateEvent,
    ) -> CorporateEvent:

        return deepcopy(corporate_event)