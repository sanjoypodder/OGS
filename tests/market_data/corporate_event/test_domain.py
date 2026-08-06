"""
Tests for CorporateEvent domain.
"""

from ogs.market_data.corporate_event import (
    CorporateEvent,
    CorporateEventStatus,
    CorporateEventType,
)


def test_default():

    event = CorporateEvent()

    assert event.corporate_event_id == ""
    assert event.exchange == ""
    assert event.market == ""
    assert event.instrument == ""
    assert event.event_name == ""
    assert event.description == ""

    assert (
        event.corporate_event_type
        == CorporateEventType.UNKNOWN
    )

    assert (
        event.status
        == CorporateEventStatus.UNKNOWN
    )

    assert event.active

    assert not event.is_valid
    assert not event.is_active


def test_valid():

    event = CorporateEvent(
        corporate_event_id="EV001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
        event_name="Dividend",
    )

    assert event.is_valid


def test_active():

    event = CorporateEvent(
        corporate_event_id="EV001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
        event_name="Dividend",
        status=CorporateEventStatus.ACTIVE,
    )

    assert event.is_active


def test_to_dict():

    event = CorporateEvent(
        corporate_event_id="EV001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
        event_name="Dividend",
    )

    data = event.to_dict()

    assert data["corporate_event_id"] == "EV001"
    assert data["exchange"] == "NSE"
    assert data["market"] == "Equity"
    assert data["instrument"] == "INFY"
    assert data["event_name"] == "Dividend"


def test_string():

    event = CorporateEvent(
        corporate_event_id="EV001",
        event_name="Dividend",
    )

    assert "CorporateEvent" in str(event)