"""
===========================================================

OGS Smart Money AI

MSS Validation Rule Tests

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


def test_candidate_requires_mss():

    validator = OrderBlockCandidateValidator()

    candidate = replace(
        make_bullish_order_block_candidate(),
        mss=None,
    )

    result = validator.validate(candidate)

    assert result.status == ValidationStatus.INVALID
    assert result.reason == "MSS required"


def test_candidate_with_mss():

    validator = OrderBlockCandidateValidator()

    candidate = make_bullish_order_block_candidate()

    result = validator.validate(candidate)

    assert result.status == ValidationStatus.VALID