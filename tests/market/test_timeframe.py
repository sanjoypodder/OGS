from ogs.market.timeframe import Timeframe


def test_value():
    assert Timeframe.M5.value == "5m"


def test_minutes():
    assert Timeframe.H1.minutes == 60
    assert Timeframe.H4.minutes == 240


def test_seconds():
    assert Timeframe.M15.seconds == 900


def test_label():
    assert Timeframe.D1.label == "1 Day"


def test_intraday():
    assert Timeframe.H1.is_intraday
    assert not Timeframe.W1.is_intraday


def test_higher_timeframe():
    assert Timeframe.D1.is_higher_timeframe
    assert not Timeframe.M5.is_higher_timeframe


def test_next_higher():
    assert Timeframe.M5.next_higher == Timeframe.M15
    assert Timeframe.H4.next_higher == Timeframe.D1
    assert Timeframe.MN1.next_higher is None
