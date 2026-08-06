"""
Tests for QuoteValidator.
"""

from datetime import UTC
from datetime import datetime

import pytest

from ogs.market_data.quote import (
    Quote,
    QuoteStatus,
    QuoteType,
    QuoteValidator,
)


def test_validator_accepts_valid_quote():

    quote = Quote(
        name="TEST",
        bid=100,
        ask=101,
        last=100.5,
    )

    QuoteValidator().validate(quote)


def test_validator_rejects_non_quote():

    with pytest.raises(TypeError):
        QuoteValidator().validate("quote")


def test_validator_rejects_empty_name():

    quote = Quote()

    with pytest.raises(ValueError):
        QuoteValidator().validate(quote)


@pytest.mark.parametrize(
    "field",
    [
        "bid",
        "ask",
        "last",
        "bid_size",
        "ask_size",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ],
)
def test_negative_numeric(field):

    kwargs = {
        "name": "TEST",
        field: -1,
    }

    quote = Quote(**kwargs)

    with pytest.raises(ValueError):
        QuoteValidator().validate(quote)


def test_invalid_quote_type():

    quote = Quote(
        name="TEST",
    )

    quote.quote_type = "LIVE"

    with pytest.raises(ValueError):
        QuoteValidator().validate(quote)


def test_invalid_status():

    quote = Quote(
        name="TEST",
    )

    quote.status = "ACTIVE"

    with pytest.raises(ValueError):
        QuoteValidator().validate(quote)


def test_invalid_timestamp():

    quote = Quote(
        name="TEST",
    )

    quote.timestamp = "today"

    with pytest.raises(ValueError):
        QuoteValidator().validate(quote)


def test_callable_validator():

    quote = Quote(
        name="TEST",
    )

    QuoteValidator()(quote)


def test_valid_enums():

    quote = Quote(
        name="TEST",
        quote_type=QuoteType.LIVE,
        status=QuoteStatus.ACTIVE,
    )

    QuoteValidator().validate(quote)


def test_valid_datetime():

    quote = Quote(
        name="TEST",
        timestamp=datetime.now(UTC),
    )

    QuoteValidator().validate(quote)