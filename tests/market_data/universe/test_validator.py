"""
Tests for Universe validator.
"""

import pytest

from ogs.market_data.universe import (
    Universe,
    UniverseValidator,
)


def make():

    return Universe(
        universe_id="UNI001",
        universe_name="Universe",
    )


def test_success():

    validator = UniverseValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "universe_id",
        "universe_name",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = UniverseValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_symbols():

    obj = make()

    obj.symbols = "RELIANCE"

    validator = UniverseValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_type():

    obj = make()

    obj.universe_type = "INVALID"

    validator = UniverseValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = UniverseValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)