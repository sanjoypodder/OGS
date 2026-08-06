"""
Tests for CorporateEvent collection.
"""

from ogs.market_data.corporate_event import (
    CorporateEvent,
    CorporateEventCollection,
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
        event_name="Dividend",
        corporate_event_type=event_type,
        status=status,
    )


def test_add():

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

    assert len(collection) == 1


def test_find():

    collection = CorporateEventCollection()

    event = make(
        "EV001",
        "NSE",
        "Equity",
        "INFY",
        CorporateEventType.DIVIDEND,
        CorporateEventStatus.ACTIVE,
    )

    collection.add(event)

    assert collection.find("EV001") == event
    assert collection.find("UNKNOWN") is None


def test_by_exchange():

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
            "NYSE",
            "Equity",
            "AAPL",
            CorporateEventType.EARNINGS,
            CorporateEventStatus.ACTIVE,
        )
    )

    assert len(collection.by_exchange("NSE")) == 1


def test_by_market():

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

    assert len(collection.by_market("Equity")) == 1


def test_by_instrument():

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

    assert len(collection.by_instrument("INFY")) == 1


def test_by_event_type():

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

    assert (
        len(
            collection.by_event_type(
                CorporateEventType.DIVIDEND
            )
        )
        == 1
    )


def test_by_status():

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

    assert (
        len(
            collection.by_status(
                CorporateEventStatus.ACTIVE
            )
        )
        == 1
    )


def test_active():

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
            "NYSE",
            "Equity",
            "AAPL",
            CorporateEventType.EARNINGS,
            CorporateEventStatus.COMPLETED,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

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

    assert len(collection.to_list()) == 1