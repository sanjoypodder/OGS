"""
Tests for TradingSessionTemplate domain.
"""

from datetime import time

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def test_default():

    session = TradingSessionTemplate()

    assert session.trading_session_template_id == ""
    assert session.template_name == ""
    assert session.exchange == ""
    assert session.market == ""
    assert session.timezone == ""

    assert session.open_time == time(9, 15)
    assert session.close_time == time(15, 30)

    assert session.trading_days == [
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
    ]

    assert (
        session.session_type
        == TradingSessionTemplateType.UNKNOWN
    )

    assert (
        session.status
        == TradingSessionTemplateStatus.UNKNOWN
    )

    assert session.active

    assert not session.is_valid
    assert not session.is_active


def test_valid():

    session = TradingSessionTemplate(
        trading_session_template_id="TST001",
        template_name="NSE Regular",
        exchange="NSE",
        market="Equity",
        timezone="Asia/Kolkata",
    )

    assert session.is_valid


def test_active():

    session = TradingSessionTemplate(
        trading_session_template_id="TST001",
        template_name="NSE Regular",
        exchange="NSE",
        market="Equity",
        timezone="Asia/Kolkata",
        status=TradingSessionTemplateStatus.ACTIVE,
    )

    assert session.is_active


def test_to_dict():

    session = TradingSessionTemplate(
        trading_session_template_id="TST001",
        template_name="NSE Regular",
        exchange="NSE",
        market="Equity",
        timezone="Asia/Kolkata",
    )

    data = session.to_dict()

    assert (
        data["trading_session_template_id"]
        == "TST001"
    )

    assert data["template_name"] == "NSE Regular"
    assert data["exchange"] == "NSE"
    assert data["market"] == "Equity"
    assert data["timezone"] == "Asia/Kolkata"


def test_string():

    session = TradingSessionTemplate(
        trading_session_template_id="TST001",
        template_name="NSE Regular",
    )

    assert "TradingSessionTemplate" in str(session)