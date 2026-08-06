"""
Tests for Metadata validator.
"""

import pytest

from ogs.market_data.metadata import (
    Metadata,
    MetadataValidator,
)


def make():

    return Metadata(
        metadata_id="MD001",
        entity_type="Instrument",
        entity_id="INFY",
        key="sector",
    )


def test_success():

    validator = MetadataValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "metadata_id",
        "entity_type",
        "entity_id",
        "key",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = MetadataValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_metadata_type():

    obj = make()

    obj.metadata_type = "INVALID"

    validator = MetadataValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_value_type():

    obj = make()

    obj.value_type = "INVALID"

    validator = MetadataValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = MetadataValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)