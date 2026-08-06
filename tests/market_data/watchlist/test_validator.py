"""
Tests for Watchlist validator.
"""

import pytest

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistValidator,
)


def make():

    return Watchlist(
        watchlist_id="WL001",
        watchlist_name="Swing",
    )


def test_success():

    validator = WatchlistValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "watchlist_id",
        "watchlist_name",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = WatchlistValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_symbols():

    obj = make()

    obj.symbols = "RELIANCE"

    validator = WatchlistValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_watchlist_type():

    obj = make()

    obj.watchlist_type = "INVALID"

    validator = WatchlistValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = WatchlistValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)