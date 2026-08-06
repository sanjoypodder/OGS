"""
===========================================================

OGS Smart Money AI

Imbalance Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import Imbalance


class ImbalanceValidator(BaseValidator[Imbalance]):
    """
    Validate an imbalance.
    """

    def validate(
        self,
        imbalance: Imbalance,
    ) -> bool:

        if imbalance is None:
            return False

        if imbalance.first is None:
            return False

        if imbalance.middle is None:
            return False

        if imbalance.last is None:
            return False

        if imbalance.direction is None:
            return False

        return True