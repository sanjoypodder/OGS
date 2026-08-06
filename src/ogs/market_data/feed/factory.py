"""
OGS Smart Money AI

Feed Factory
"""

from __future__ import annotations

from datetime import UTC, datetime

from ogs.framework import BaseFactory

from .domain import Feed
from .enums import (
    FeedStatus,
    FeedType,
)
from .validator import FeedValidator


class FeedFactory(BaseFactory):
    """
    Factory for Feed objects.
    """

    _validator = FeedValidator()

    @classmethod
    def create(
        cls,
        *,
        name: str,
        feed_type: FeedType = FeedType.UNKNOWN,
        status: FeedStatus = FeedStatus.UNKNOWN,
        provider: str = "",
        symbol: str = "",
        timeframe: str = "",
        latency_ms: float = 0.0,
        update_count: int = 0,
        last_price: float = 0.0,
        last_updated: datetime | None = None,
    ) -> Feed:

        feed = Feed(
            name=name,
            feed_type=feed_type,
            status=status,
            provider=provider,
            symbol=symbol,
            timeframe=timeframe,
            latency_ms=latency_ms,
            update_count=update_count,
            last_price=last_price,
            last_updated=(
                last_updated
                if last_updated is not None
                else datetime.now(UTC)
            ),
        )

        return cls._validator(feed)

    @classmethod
    def live(
        cls,
        name: str,
    ) -> Feed:
        return cls.create(
            name=name,
            feed_type=FeedType.LIVE,
            status=FeedStatus.CONNECTED,
        )

    @classmethod
    def historical(
        cls,
        name: str,
    ) -> Feed:
        return cls.create(
            name=name,
            feed_type=FeedType.HISTORICAL,
            status=FeedStatus.CONNECTED,
        )

    @classmethod
    def simulated(
        cls,
        name: str,
    ) -> Feed:
        return cls.create(
            name=name,
            feed_type=FeedType.SIMULATED,
            status=FeedStatus.CONNECTED,
        )

    @classmethod
    def clone(
        cls,
        feed: Feed,
    ) -> Feed:
        return cls.create(
            name=feed.name,
            feed_type=feed.feed_type,
            status=feed.status,
            provider=feed.provider,
            symbol=feed.symbol,
            timeframe=feed.timeframe,
            latency_ms=feed.latency_ms,
            update_count=feed.update_count,
            last_price=feed.last_price,
            last_updated=feed.last_updated,
        )