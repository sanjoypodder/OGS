from datetime import time

from ogs.market.session import TradingSession


def test_session_name():
    assert TradingSession.LONDON.value == "London"


def test_start_time():
    assert TradingSession.LONDON.start == time(8, 0)


def test_end_time():
    assert TradingSession.NEW_YORK.end == time(22, 0)


def test_active():
    assert TradingSession.ASIAN.is_active
    assert not TradingSession.CLOSED.is_active


def test_label():
    assert TradingSession.LONDON.label == "London"