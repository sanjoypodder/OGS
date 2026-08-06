"""
OGS Smart Money AI

Tick Factory
"""

from __future__ import annotations

from datetime import UTC, datetime

from ogs.framework import BaseFactory

from .domain import Tick
from .enums import ProviderType
from .validator import TickValidator


class TickFactory(BaseFactory):
    """
    Factory responsible for creating Tick domain objects.

    Every Tick instance produced by this factory is validated
    before being returned.
    """

    validator = TickValidator()

    @classmethod
    def create(
        cls,
        symbol: str,
        timestamp: datetime,
        bid: float,
        ask: float,
        last: float,
        volume: float = 0.0,
        provider: ProviderType = ProviderType.UNKNOWN,
    ) -> Tick:
        """
        Create and validate a Tick instance.
        """

        tick = Tick(
            symbol=symbol.strip().upper(),
            timestamp=timestamp,
            bid=float(bid),
            ask=float(ask),
            last=float(last),
            volume=float(volume),
            provider=provider,
        )

        if not cls.validator(tick):
            raise ValueError("Invalid Tick.")

        return tick

    @classmethod
    def from_bid_ask(
        cls,
        symbol: str,
        bid: float,
        ask: float,
        timestamp: datetime | None = None,
        provider: ProviderType = ProviderType.UNKNOWN,
    ) -> Tick:
        """
        Create a Tick from bid/ask prices.
        """

        timestamp = timestamp or datetime.now(UTC)

        return cls.create(
            symbol=symbol,
            timestamp=timestamp,
            bid=bid,
            ask=ask,
            last=(bid + ask) / 2,
            volume=0.0,
            provider=provider,
        )

    @classmethod
    def from_trade(
        cls,
        symbol: str,
        price: float,
        volume: float,
        timestamp: datetime | None = None,
        provider: ProviderType = ProviderType.UNKNOWN,
    ) -> Tick:
        """
        Create a Tick from a trade execution.
        """

        timestamp = timestamp or datetime.now(UTC)

        return cls.create(
            symbol=symbol,
            timestamp=timestamp,
            bid=price,
            ask=price,
            last=price,
            volume=volume,
            provider=provider,
        )

    @classmethod
    def simulated(
        cls,
        symbol: str,
        price: float,
        volume: float = 1.0,
    ) -> Tick:
        """
        Create a simulated Tick.
        """

        return cls.create(
            symbol=symbol,
            timestamp=datetime.now(UTC),
            bid=price,
            ask=price,
            last=price,
            volume=volume,
            provider=ProviderType.SIMULATION,
        )

    @classmethod
    def clone(
        cls,
        tick: Tick,
    ) -> Tick:
        """
        Create a copy of an existing Tick.
        """

        return cls.create(
            symbol=tick.symbol,
            timestamp=tick.timestamp,
            bid=tick.bid,
            ask=tick.ask,
            last=tick.last,
            volume=tick.volume,
            provider=tick.provider,
        )