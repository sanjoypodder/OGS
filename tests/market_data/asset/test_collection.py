"""
Tests for Asset collection.
"""

from ogs.market_data.asset import (
    Asset,
    AssetCollection,
    AssetType,
)


def make(asset_id, asset_type):

    return Asset(
        asset_id=asset_id,
        symbol=asset_id,
        name=asset_id,
        asset_type=asset_type,
    )


def test_collection():

    c = AssetCollection()

    c.add(make("AAPL", AssetType.EQUITY))

    assert len(c) == 1


def test_find():

    c = AssetCollection()

    asset = make("BTC", AssetType.CRYPTO)

    c.add(asset)

    assert c.find("BTC") == asset
    assert c.find("NONE") is None


def test_filters():

    c = AssetCollection()

    c.add(make("AAPL", AssetType.EQUITY))
    c.add(make("BTC", AssetType.CRYPTO))
    c.add(make("EURUSD", AssetType.FOREX))
    c.add(make("XAU", AssetType.COMMODITY))

    assert len(c.equities()) == 1
    assert len(c.crypto()) == 1
    assert len(c.forex()) == 1
    assert len(c.commodities()) == 1


def test_active():

    c = AssetCollection()

    a = make("BTC", AssetType.CRYPTO)

    a.active = False

    c.add(a)

    assert len(c.active()) == 0
    assert len(c.inactive()) == 1


def test_to_list():

    c = AssetCollection()

    c.add(make("BTC", AssetType.CRYPTO))

    assert len(c.to_list()) == 1