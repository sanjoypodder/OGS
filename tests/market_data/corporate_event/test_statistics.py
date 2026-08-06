"""
Tests for CorporateEvent statistics.
"""

from ogs.market_data.corporate_event import (
    CorporateEvent,
    CorporateEventCollection,
    CorporateEventStatistics,
    CorporateEventStatus,
    CorporateEventType,
)


def make(
    event_id,
    exchange,
    market,
    instrument,
    event_type,
    status,
):

    return CorporateEvent(
        corporate_event_id=event_id,
        exchange=exchange,
        market=market,
        instrument=instrument,
        event_name=event_type.name,
        corporate_event_type=event_type,
        status=status,
    )


def build_collection():

    collection = CorporateEventCollection()

    collection.add(
        make(
            "EV001",
            "NSE",
            "Equity",
            "INFY",
            CorporateEventType.DIVIDEND,
            CorporateEventStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "EV002",
            "NSE",
            "Equity",
            "TCS",
            CorporateEventType.EARNINGS,
            CorporateEventStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "EV003",
            "NYSE",
            "Equity",
            "AAPL",
            CorporateEventType.BUYBACK,
            CorporateEventStatus.COMPLETED,
        )
    )

    return collection


def test_counts():

    stats = CorporateEventStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2


def test_exchange_distribution():

    stats = CorporateEventStatistics(
        build_collection()
    )

    distribution = (
        stats.exchange_distribution()
    )

    assert distribution["NSE"] == 2
    assert distribution["NYSE"] == 1


def test_market_distribution():

    stats = CorporateEventStatistics(
        build_collection()
    )

    distribution = (
        stats.market_distribution()
    )

    assert distribution["Equity"] == 3


def test_event_type_distribution():

    stats = CorporateEventStatistics(
        build_collection()
    )

    distribution = (
        stats.event_type_distribution()
    )

    assert distribution["DIVIDEND"] == 1
    assert distribution["EARNINGS"] == 1
    assert distribution["BUYBACK"] == 1


def test_status_distribution():

    stats = CorporateEventStatistics(
        build_collection()
    )

    distribution = (
        stats.status_distribution()
    )

    assert distribution["ACTIVE"] == 2
    assert distribution["COMPLETED"] == 1


def test_summary():

    stats = CorporateEventStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2