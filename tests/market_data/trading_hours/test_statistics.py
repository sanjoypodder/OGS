"""
Tests for TradingHours statistics.
"""

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursCollection,
    TradingHoursStatistics,
    TradingHoursStatus,
    TradingHoursType,
)


def make(
    trading_hours_id,
    exchange,
    market,
    trading_hours_type,
    status,
):

    return TradingHours(
        trading_hours_id=trading_hours_id,
        exchange=exchange,
        market=market,
        session_name="Regular",
        trading_hours_type=trading_hours_type,
        status=status,
    )


def build_collection():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TH002",
            "NSE",
            "Derivatives",
            TradingHoursType.POST_MARKET,
            TradingHoursStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TH003",
            "NYSE",
            "Equity",
            TradingHoursType.PRE_MARKET,
            TradingHoursStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = TradingHoursStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2


def test_exchange_distribution():

    stats = TradingHoursStatistics(
        build_collection()
    )

    distribution = stats.exchange_distribution()

    assert distribution["NSE"] == 2
    assert distribution["NYSE"] == 1


def test_market_distribution():

    stats = TradingHoursStatistics(
        build_collection()
    )

    distribution = stats.market_distribution()

    assert distribution["Equity"] == 2
    assert distribution["Derivatives"] == 1


def test_type_distribution():

    stats = TradingHoursStatistics(
        build_collection()
    )

    distribution = stats.type_distribution()

    assert distribution["REGULAR"] == 1
    assert distribution["POST_MARKET"] == 1
    assert distribution["PRE_MARKET"] == 1


def test_summary():

    stats = TradingHoursStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2