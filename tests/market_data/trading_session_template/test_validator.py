"""
Tests for TradingSessionTemplate validator.
"""

import pytest

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateValidator,
)


def make():

    return TradingSessionTemplate(
        trading_session_template_id="TST001",
        template_name="NSE Regular",
        exchange="NSE",
        market="Equity",
        timezone="Asia/Kolkata",
    )


def test_success():

    validator = TradingSessionTemplateValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "trading_session_template_id",
        "template_name",
        "exchange",
        "market",
        "timezone",
    ],
)
def test_required_fields(field):

    session = make()

    setattr(session, field, "")

    validator = TradingSessionTemplateValidator()

    with pytest.raises(ValueError):
        validator.validate(session)


def test_invalid_days():

    session = make()

    session.trading_days = "MON"

    validator = TradingSessionTemplateValidator()

    with pytest.raises(ValueError):
        validator.validate(session)


def test_invalid_type():

    session = make()

    session.session_type = "INVALID"

    validator = TradingSessionTemplateValidator()

    with pytest.raises(ValueError):
        validator.validate(session)


def test_invalid_status():

    session = make()

    session.status = "INVALID"

    validator = TradingSessionTemplateValidator()

    with pytest.raises(ValueError):
        validator.validate(session)