"""
Tests for Asset validator.
"""

import pytest

from ogs.market_data.asset import (
    Asset,
    AssetType,
    AssetValidator,
)


def valid_asset():

    return Asset(
        asset_id="AAPL",
        symbol="AAPL",
        name="Apple Inc.",
        asset_type=AssetType.EQUITY,
    )


def test_validator_success():

    assert AssetValidator()(valid_asset())


@pytest.mark.parametrize(
    "field,value",
    [
        ("asset_id", ""),
        ("symbol", ""),
        ("name", ""),
    ],
)
def test_required_fields(field, value):

    asset = valid_asset()

    setattr(asset, field, value)

    with pytest.raises(ValueError):
        AssetValidator()(asset)


def test_invalid_asset_type():

    asset = valid_asset()

    asset.asset_type = "EQUITY"

    with pytest.raises(ValueError):
        AssetValidator()(asset)


def test_invalid_currency():

    asset = valid_asset()

    asset.currency = ""

    with pytest.raises(ValueError):
        AssetValidator()(asset)


def test_invalid_active():

    asset = valid_asset()

    asset.active = None

    with pytest.raises(ValueError):
        AssetValidator()(asset)


def test_invalid_created():

    asset = valid_asset()

    asset.created_at = None

    with pytest.raises(ValueError):
        AssetValidator()(asset)


def test_invalid_updated():

    asset = valid_asset()

    asset.updated_at = None

    with pytest.raises(ValueError):
        AssetValidator()(asset)