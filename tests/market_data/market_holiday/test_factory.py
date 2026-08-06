"""
Tests for MarketHoliday factory.
"""

from ogs.market_data.market_holiday import (
    MarketHoliday,
    MarketHolidayFactory,
    MarketHolidayStatus,
    MarketHolidayType,
)


def test_create():

    holiday = MarketHolidayFactory.create(
        market_holiday_id="HOL001"
    )

    assert isinstance(
        holiday,
        MarketHoliday,
    )


def test_national():

    holiday = MarketHolidayFactory.national()

    assert (
        holiday.holiday_type
        == MarketHolidayType.NATIONAL
    )

    assert (
        holiday.status
        == MarketHolidayStatus.ACTIVE
    )


def test_exchange():

    holiday = MarketHolidayFactory.exchange()

    assert (
        holiday.holiday_type
        == MarketHolidayType.EXCHANGE
    )


def test_bank():

    holiday = MarketHolidayFactory.bank()

    assert (
        holiday.holiday_type
        == MarketHolidayType.BANK
    )


def test_religious():

    holiday = MarketHolidayFactory.religious()

    assert (
        holiday.holiday_type
        == MarketHolidayType.RELIGIOUS
    )


def test_public():

    holiday = MarketHolidayFactory.public()

    assert (
        holiday.holiday_type
        == MarketHolidayType.PUBLIC
    )


def test_special_trading():

    holiday = (
        MarketHolidayFactory.special_trading()
    )

    assert (
        holiday.holiday_type
        == MarketHolidayType.SPECIAL_TRADING
    )


def test_half_day():

    holiday = MarketHolidayFactory.half_day()

    assert (
        holiday.holiday_type
        == MarketHolidayType.HALF_DAY
    )


def test_emergency():

    holiday = MarketHolidayFactory.emergency()

    assert (
        holiday.holiday_type
        == MarketHolidayType.EMERGENCY
    )


def test_custom():

    holiday = MarketHolidayFactory.custom()

    assert (
        holiday.holiday_type
        == MarketHolidayType.CUSTOM
    )


def test_clone():

    holiday = MarketHolidayFactory.create(
        market_holiday_id="HOL001"
    )

    clone = MarketHolidayFactory.clone(
        holiday
    )

    assert clone == holiday
    assert clone is not holiday