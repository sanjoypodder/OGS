"""
OGS Smart Money AI

Feed Collection
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from ogs.framework import BaseCollection

from .domain import Feed
from .enums import (
    FeedStatus,
    FeedType,
)


class FeedCollection(BaseCollection):
    """
    Collection of Feed objects.
    """

    def __init__(
        self,
        feeds: Iterable[Feed] = (),
    ) -> None:
        self._feeds = list(feeds)

    def __iter__(self) -> Iterator[Feed]:
        return iter(self._feeds)

    def __len__(self) -> int:
        return len(self._feeds)

    def __getitem__(self, index: int) -> Feed:
        return self._feeds[index]

    def add(
        self,
        feed: Feed,
    ) -> None:
        self._feeds.append(feed)

    def connected(self) -> "FeedCollection":
        return FeedCollection(
            feed
            for feed in self._feeds
            if feed.status == FeedStatus.CONNECTED
        )

    def disconnected(self) -> "FeedCollection":
        return FeedCollection(
            feed
            for feed in self._feeds
            if feed.status == FeedStatus.DISCONNECTED
        )

    def by_type(
        self,
        feed_type: FeedType,
    ) -> "FeedCollection":
        return FeedCollection(
            feed
            for feed in self._feeds
            if feed.feed_type == feed_type
        )

    def by_provider(
        self,
        provider: str,
    ) -> "FeedCollection":
        return FeedCollection(
            feed
            for feed in self._feeds
            if feed.provider == provider
        )

    def fastest(self) -> Feed | None:
        if not self._feeds:
            return None

        return min(
            self._feeds,
            key=lambda feed: feed.latency_ms,
        )

    def slowest(self) -> Feed | None:
        if not self._feeds:
            return None

        return max(
            self._feeds,
            key=lambda feed: feed.latency_ms,
        )

    def average_latency(self) -> float:
        if not self._feeds:
            return 0.0

        return (
            sum(
                feed.latency_ms
                for feed in self._feeds
            )
            / len(self._feeds)
        )

    def total_updates(self) -> int:
        return sum(
            feed.update_count
            for feed in self._feeds
        )

    def find(
        self,
        name: str,
    ) -> Feed | None:
        name = name.casefold()

        for feed in self._feeds:
            if feed.name.casefold() == name:
                return feed

        return None

    def to_list(self) -> list[Feed]:
        return list(self._feeds)