"""
Tests for Calendar validator.
"""

from datetime import date

import pytest

from ogs.market_data.calendar import (
    Calendar,
    CalendarValidator,
)


def make():

    return Calendar(
        calendar_id="CAL001",
        exchange="NSE",
        market="Cash",
        trading_date=date.today(),
    )


def test_success():

    validator = CalendarValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "calendar_id",
        "exchange",
        "market",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = CalendarValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_missing_date():

    obj = make()

    obj.trading_date = None

    validator = CalendarValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_date_type():

    obj = make()

    obj.trading_date = "2026-01-01"

    validator = CalendarValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)