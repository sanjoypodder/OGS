"""
OGS Smart Money AI

Tick Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Tick
from .enums import ProviderType


class TickValidator(BaseValidator):
    """
    Validator for Tick domain objects.

    This validator performs structural validation only.
    It verifies that a Tick instance contains valid values
    and does not attempt to validate market logic.
    """

    def validate(self, tick: Tick | None) -> bool:
        """
        Validate a Tick object.

        Parameters
        ----------
        tick : Tick | None
            Tick instance to validate.

        Returns
        -------
        bool
            True if the tick is valid, otherwise False.
        """

        if not isinstance(tick, Tick):
            return False

        if not self._validate_symbol(tick.symbol):
            return False

        if not self._validate_timestamp(tick.timestamp):
            return False

        if not self._validate_prices(
            bid=tick.bid,
            ask=tick.ask,
            last=tick.last,
        ):
            return False

        if not self._validate_volume(tick.volume):
            return False

        if not self._validate_provider(tick.provider):
            return False

        return True

    @staticmethod
    def _validate_symbol(symbol: str) -> bool:
        """
        Validate the trading symbol.
        """

        return isinstance(symbol, str) and bool(symbol.strip())

    @staticmethod
    def _validate_timestamp(timestamp: datetime) -> bool:
        """
        Validate timestamp.
        """

        return isinstance(timestamp, datetime)

    @staticmethod
    def _validate_prices(
        *,
        bid: float,
        ask: float,
        last: float,
    ) -> bool:
        """
        Validate price fields.
        """

        if bid < 0:
            return False

        if ask < 0:
            return False

        if last < 0:
            return False

        if ask < bid:
            return False

        return True

    @staticmethod
    def _validate_volume(volume: float) -> bool:
        """
        Validate traded volume.
        """

        return volume >= 0

    @staticmethod
    def _validate_provider(provider: ProviderType) -> bool:
        """
        Validate provider type.
        """

        return isinstance(provider, ProviderType)