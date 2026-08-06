"""
===========================================================

OGS Smart Money AI

Fair Value Gap Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import FairValueGap


class FairValueGapValidator(BaseValidator):
    """
    Validate Fair Value Gaps.
    """

    def validate(
        self,
        gap: FairValueGap,
    ) -> bool:

        if gap is None:
            return False

        if gap.first is None:
            return False

        if gap.middle is None:
            return False

        if gap.last is None:
            return False

        if gap.direction is None:
            return False

        if gap.top < gap.bottom:
            return False

        if gap.size < 0:
            return False

        return True