"""
Tests for TradingHours validator.
"""

import pytest

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursValidator,
)


def make():

    return TradingHours(
        trading_hours_id="TH001",
        exchange="NSE",
        market="Equity",
        session_name="Regular",
    )


def test_success():

    validator = TradingHoursValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "trading_hours_id",
        "exchange",
        "market",
        "session_name",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = TradingHoursValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_type():

    obj = make()

    obj.trading_hours_type = "INVALID"

    validator = TradingHoursValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = TradingHoursValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)