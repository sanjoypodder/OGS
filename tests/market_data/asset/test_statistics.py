"""
Tests for Asset statistics.
"""

from ogs.market_data.asset import (
    Asset,
    AssetCollection,
    AssetStatistics,
    AssetType,
)


def make_collection():

    c = AssetCollection()

    c.add(
        Asset(
            asset_id="AAPL",
            symbol="AAPL",
            name="Apple",
            asset_type=AssetType.EQUITY,
        )
    )

    c.add(
        Asset(
            asset_id="BTC",
            symbol="BTC",
            name="Bitcoin",
            asset_type=AssetType.CRYPTO,
        )
    )

    return c


def test_counts():

    stats = AssetStatistics(make_collection())

    assert stats.count == 2
    assert stats.active_count == 2


def test_distribution():

    stats = AssetStatistics(make_collection())

    assert stats.equity_count == 1
    assert stats.crypto_count == 1


def test_summary():

    stats = AssetStatistics(make_collection())

    summary = stats.summary()

    assert summary["count"] == 2
    assert summary["equity_count"] == 1