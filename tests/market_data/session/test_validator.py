"""
Tests for Session validator.
"""

import pytest

from ogs.market_data.session import (
    Session,
    SessionValidator,
)


def make():

    return Session(
        session_id="1",
        name="Regular",
        exchange="NSE",
        market="Cash",
    )


def test_success():

    validator = SessionValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "session_id",
        "name",
        "exchange",
        "market",
    ],
)
def test_required(field):

    obj = make()

    setattr(obj, field, "")

    validator = SessionValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_invalid_timezone():

    obj = make()

    obj.timezone = ""

    validator = SessionValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)