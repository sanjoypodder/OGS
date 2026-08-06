"""
Tests for Index validator.
"""

import pytest

from ogs.market_data.index import (
    Index,
    IndexValidator,
)


def make():

    return Index(
        index_code="NIFTY50",
        index_name="NIFTY 50",
        exchange="NSE",
    )


def test_success():

    validator = IndexValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "index_code",
        "index_name",
        "exchange",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = IndexValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_invalid_base_value():

    obj = make()

    obj.base_value = -1

    validator = IndexValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_invalid_current_value():

    obj = make()

    obj.current_value = -1

    validator = IndexValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_invalid_constituent_count():

    obj = make()

    obj.constituent_count = -1

    validator = IndexValidator()

    with pytest.raises(ValueError):
        validator.validate(obj) 