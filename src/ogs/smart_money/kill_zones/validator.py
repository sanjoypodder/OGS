"""
OGS Smart Money AI
------------------

Kill Zone Validator

Validates Kill Zone domain objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import KillZone


class KillZoneValidator(
    BaseValidator[KillZone],
):
    """
    Validator for KillZone objects.
    """

    def validate(
        self,
        zone: KillZone,
    ) -> bool:
        """
        Validate a KillZone instance.
        """

        if zone is None:
            return False

        if not zone.symbol:
            return False

        if zone.zone is None:
            return False

        if zone.session is None:
            return False

        if zone.status is None:
            return False

        if zone.timezone is None:
            return False

        if zone.start_time is None:
            return False

        if zone.end_time is None:
            return False

        if zone.end_time <= zone.start_time:
            return False

        if zone.duration_seconds <= 0:
            return False

        return True