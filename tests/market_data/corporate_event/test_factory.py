"""
Tests for CorporateEvent factory.
"""

from ogs.market_data.corporate_event import (
    CorporateEvent,
    CorporateEventFactory,
    CorporateEventStatus,
    CorporateEventType,
)


def test_create():

    event = CorporateEventFactory.create(
        corporate_event_id="EV001"
    )

    assert isinstance(event, CorporateEvent)


def test_earnings():

    event = CorporateEventFactory.earnings()

    assert (
        event.corporate_event_type
        == CorporateEventType.EARNINGS
    )

    assert (
        event.status
        == CorporateEventStatus.ACTIVE
    )


def test_dividend():

    event = CorporateEventFactory.dividend()

    assert (
        event.corporate_event_type
        == CorporateEventType.DIVIDEND
    )


def test_stock_split():

    event = CorporateEventFactory.stock_split()

    assert (
        event.corporate_event_type
        == CorporateEventType.STOCK_SPLIT
    )


def test_bonus():

    event = CorporateEventFactory.bonus()

    assert (
        event.corporate_event_type
        == CorporateEventType.BONUS
    )


def test_rights():

    event = CorporateEventFactory.rights()

    assert (
        event.corporate_event_type
        == CorporateEventType.RIGHTS
    )


def test_merger():

    event = CorporateEventFactory.merger()

    assert (
        event.corporate_event_type
        == CorporateEventType.MERGER
    )


def test_acquisition():

    event = CorporateEventFactory.acquisition()

    assert (
        event.corporate_event_type
        == CorporateEventType.ACQUISITION
    )


def test_ipo():

    event = CorporateEventFactory.ipo()

    assert (
        event.corporate_event_type
        == CorporateEventType.IPO
    )


def test_buyback():

    event = CorporateEventFactory.buyback()

    assert (
        event.corporate_event_type
        == CorporateEventType.BUYBACK
    )


def test_custom():

    event = CorporateEventFactory.custom()

    assert (
        event.corporate_event_type
        == CorporateEventType.CUSTOM
    )


def test_clone():

    event = CorporateEventFactory.create(
        corporate_event_id="EV001"
    )

    clone = CorporateEventFactory.clone(event)

    assert clone == event
    assert clone is not event