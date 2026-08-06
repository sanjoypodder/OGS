"""
OGS Smart Money AI

Feed Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Feed
from .enums import (
    FeedStatus,
    FeedType,
)


class FeedValidator(BaseValidator):
    """
    Feed validator.
    """

    def validate(
        self,
        feed: Feed,
    ) -> None:

        if not isinstance(feed, Feed):
            raise TypeError(
                "feed must be Feed."
            )

        if not feed.name.strip():
            raise ValueError(
                "Feed name cannot be empty."
            )

        if not isinstance(
            feed.feed_type,
            FeedType,
        ):
            raise TypeError(
                "Invalid feed type."
            )

        if not isinstance(
            feed.status,
            FeedStatus,
        ):
            raise TypeError(
                "Invalid feed status."
            )

        if feed.latency_ms < 0:
            raise ValueError(
                "Latency cannot be negative."
            )

        if feed.update_count < 0:
            raise ValueError(
                "Update count cannot be negative."
            )

        if feed.last_price < 0:
            raise ValueError(
                "Last price cannot be negative."
            )

        if not isinstance(
            feed.last_updated,
            datetime,
        ):
            raise TypeError(
                "Invalid datetime."
            )

    def __call__(
        self,
        feed: Feed,
    ) -> Feed:

        self.validate(feed)

        return feed