"""
===========================================================

OGS Smart Money AI

Origin Candle Validation Rule Tests

===========================================================
"""

from dataclasses import replace

from ogs.validation import ValidationStatus

from ogs.smart_money.order_block.validation import (
    OrderBlockCandidateValidator,
)

from tests.factories import (
    make_bullish_order_block_candidate,
)


def test_origin_required():

    validator = OrderBlockCandidateValidator()

    candidate = replace(
        make_bullish_order_block_candidate(),
        origin_candle=None,
    )

    result = validator.validate(candidate)

    assert result.status == ValidationStatus.INVALID
    assert result.reason == "Origin candle required"


def test_origin_present():

    validator = OrderBlockCandidateValidator()

    candidate = make_bullish_order_block_candidate()

    result = validator.validate(candidate)

    assert result.status == ValidationStatus.VALID