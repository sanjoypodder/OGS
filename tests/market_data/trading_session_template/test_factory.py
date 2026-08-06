"""
Tests for TradingSessionTemplate factory.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateFactory,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def test_create():

    session = TradingSessionTemplateFactory.create(
        trading_session_template_id="TST001"
    )

    assert isinstance(
        session,
        TradingSessionTemplate,
    )


def test_regular():

    session = TradingSessionTemplateFactory.regular()

    assert (
        session.session_type
        == TradingSessionTemplateType.REGULAR
    )

    assert (
        session.status
        == TradingSessionTemplateStatus.ACTIVE
    )


def test_pre_market():

    session = TradingSessionTemplateFactory.pre_market()

    assert (
        session.session_type
        == TradingSessionTemplateType.PRE_MARKET
    )


def test_post_market():

    session = TradingSessionTemplateFactory.post_market()

    assert (
        session.session_type
        == TradingSessionTemplateType.POST_MARKET
    )


def test_overnight():

    session = TradingSessionTemplateFactory.overnight()

    assert (
        session.session_type
        == TradingSessionTemplateType.OVERNIGHT
    )


def test_auction():

    session = TradingSessionTemplateFactory.auction()

    assert (
        session.session_type
        == TradingSessionTemplateType.AUCTION
    )


def test_extended():

    session = TradingSessionTemplateFactory.extended()

    assert (
        session.session_type
        == TradingSessionTemplateType.EXTENDED
    )


def test_special():

    session = TradingSessionTemplateFactory.special()

    assert (
        session.session_type
        == TradingSessionTemplateType.SPECIAL
    )


def test_custom():

    session = TradingSessionTemplateFactory.custom()

    assert (
        session.session_type
        == TradingSessionTemplateType.CUSTOM
    )


def test_clone():

    session = TradingSessionTemplateFactory.create(
        trading_session_template_id="TST001"
    )

    clone = TradingSessionTemplateFactory.clone(session)

    assert clone == session
    assert clone is not session