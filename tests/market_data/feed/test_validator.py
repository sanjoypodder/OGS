"""
Tests for FeedValidator.
"""

import pytest

from ogs.market_data.feed import (
    Feed,
    FeedFactory,
    FeedValidator,
)


validator = FeedValidator()


def test_valid_feed():

    feed = FeedFactory.live(
        "Live Feed"
    )

    validator.validate(feed)


def test_empty_name():

    with pytest.raises(ValueError):

        validator.validate(
            Feed(name="")
        )


def test_negative_latency():

    with pytest.raises(ValueError):

        validator.validate(
            Feed(
                name="Feed",
                latency_ms=-1,
            )
        )


def test_negative_updates():

    with pytest.raises(ValueError):

        validator.validate(
            Feed(
                name="Feed",
                update_count=-10,
            )
        )


def test_negative_price():

    with pytest.raises(ValueError):

        validator.validate(
            Feed(
                name="Feed",
                last_price=-100,
            )
        )


def test_invalid_object():

    with pytest.raises(TypeError):

        validator.validate(
            "Feed"
        )