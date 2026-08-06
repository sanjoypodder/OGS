"""
TradingSessionTemplate Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import TradingSessionTemplate
from .enums import (
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


class TradingSessionTemplateFactory:
    """
    Trading session template factory.
    """

    @staticmethod
    def create(**kwargs):

        return TradingSessionTemplate(**kwargs)

    @staticmethod
    def regular(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.REGULAR,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def pre_market(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.PRE_MARKET,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def post_market(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.POST_MARKET,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def overnight(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.OVERNIGHT,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def auction(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.AUCTION,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def extended(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.EXTENDED,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def special(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.SPECIAL,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def custom(**kwargs):

        return TradingSessionTemplate(
            session_type=TradingSessionTemplateType.CUSTOM,
            status=TradingSessionTemplateStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        session: TradingSessionTemplate,
    ) -> TradingSessionTemplate:

        return deepcopy(session)