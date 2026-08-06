"""
Tests for Settlement validator.
"""

import pytest

from ogs.market_data.settlement import (
    Settlement,
    SettlementValidator,
)


def make():

    return Settlement(
        settlement_id="SET001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
    )


def test_success():

    validator = SettlementValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "settlement_id",
        "exchange",
        "market",
        "instrument",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = SettlementValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_cycle():

    obj = make()

    obj.settlement_cycle = "INVALID"

    validator = SettlementValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_method():

    obj = make()

    obj.settlement_method = "INVALID"

    validator = SettlementValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_type():

    obj = make()

    obj.settlement_type = "INVALID"

    validator = SettlementValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = SettlementValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)