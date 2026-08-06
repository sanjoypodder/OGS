"""
Tests for Asset domain.
"""

from ogs.market_data.asset import (
    Asset,
    AssetType,
)


def test_default_asset():

    asset = Asset()

    assert asset.asset_id == ""
    assert asset.symbol == ""
    assert asset.name == ""
    assert asset.asset_type == AssetType.UNKNOWN
    assert asset.currency == "USD"
    assert asset.country == ""
    assert asset.active is True

    assert asset.is_active
    assert not asset.is_tradable
    assert not asset.is_valid


def test_is_valid():

    asset = Asset(
        asset_id="AAPL",
        symbol="AAPL",
        name="Apple Inc.",
    )

    assert asset.is_valid


def test_is_tradable():

    asset = Asset(
        asset_id="BTC",
        symbol="BTC",
        name="Bitcoin",
        asset_type=AssetType.CRYPTO,
    )

    assert asset.is_tradable


def test_to_dict():

    asset = Asset()

    data = asset.to_dict()

    assert isinstance(data, dict)
    assert data["asset_id"] == ""


def test_str():

    asset = Asset()

    assert "Asset" in str(asset)