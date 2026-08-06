"""
Tests for CorporateAction validator.
"""

import pytest

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionValidator,
)


def make():

    return CorporateAction(
        action_id="CA001",
        symbol="RELIANCE",
        exchange="NSE",
        market="Cash",
    )


def test_success():

    validator = CorporateActionValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "action_id",
        "symbol",
        "exchange",
        "market",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = CorporateActionValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_ratio():

    obj = make()

    obj.ratio = 0

    validator = CorporateActionValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_negative_cash_amount():

    obj = make()

    obj.cash_amount = -10.0

    validator = CorporateActionValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_currency():

    obj = make()

    obj.currency = ""

    validator = CorporateActionValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)