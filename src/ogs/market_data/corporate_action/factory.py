"""
===========================================================

OGS Smart Money AI

Corporate Action Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import CorporateAction
from .enums import (
    CorporateActionStatus,
    CorporateActionType,
)


class CorporateActionFactory:
    """
    Corporate Action Factory.
    """

    @staticmethod
    def create(
        action_id: str,
        symbol: str,
        exchange: str,
        market: str,
        **kwargs,
    ) -> CorporateAction:

        return CorporateAction(
            action_id=action_id,
            symbol=symbol,
            exchange=exchange,
            market=market,
            **kwargs,
        )

    @staticmethod
    def dividend(
        action_id: str,
        symbol: str,
        exchange: str,
        market: str,
        cash_amount: float,
        **kwargs,
    ) -> CorporateAction:

        return CorporateAction(
            action_id=action_id,
            symbol=symbol,
            exchange=exchange,
            market=market,
            action_type=CorporateActionType.DIVIDEND,
            status=CorporateActionStatus.ANNOUNCED,
            cash_amount=cash_amount,
            **kwargs,
        )

    @staticmethod
    def clone(
        action: CorporateAction,
    ) -> CorporateAction:

        return deepcopy(action)