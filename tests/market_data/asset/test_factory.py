"""
Tests for Asset factory.
"""

from ogs.market_data.asset import (
    Asset,
    AssetFactory,
    AssetType,
)


def test_create():

    asset = AssetFactory.create(
        asset_id="AAPL",
        symbol="AAPL",
        name="Apple Inc.",
    )

    assert isinstance(asset, Asset)


def test_equity():

    asset = AssetFactory.equity(
        "AAPL",
        "AAPL",
        "Apple Inc.",
    )

    assert asset.asset_type == AssetType.EQUITY


def test_crypto():

    asset = AssetFactory.crypto(
        "BTC",
        "BTC",
        "Bitcoin",
    )

    assert asset.asset_type == AssetType.CRYPTO


def test_forex():

    asset = AssetFactory.forex(
        "EURUSD",
        "EURUSD",
        "Euro Dollar",
    )

    assert asset.asset_type == AssetType.FOREX


def test_commodity():

    asset = AssetFactory.commodity(
        "XAU",
        "XAU",
        "Gold",
    )

    assert asset.asset_type == AssetType.COMMODITY


def test_clone():

    asset = AssetFactory.create(
        "AAPL",
        "AAPL",
        "Apple",
    )

    clone = AssetFactory.clone(asset)

    assert clone == asset
    assert clone is not asset