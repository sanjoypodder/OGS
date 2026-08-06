"""
Tests for Screener validator.
"""

import pytest

from ogs.market_data.screener import (
    Screener,
    ScreenerValidator,
)


def make():

    return Screener(
        screener_id="SCR001",
        screener_name="SMC",
    )


def test_success():

    validator = ScreenerValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "screener_id",
        "screener_name",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = ScreenerValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_filters():

    obj = make()

    obj.filters = "volume > 100000"

    validator = ScreenerValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_sort_order():

    obj = make()

    obj.sort_order = "INVALID"

    validator = ScreenerValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_type():

    obj = make()

    obj.screener_type = "INVALID"

    validator = ScreenerValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = ScreenerValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)