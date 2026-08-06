"""
===========================================================

OGS Smart Money AI

Order Block Candidate Validator Tests

===========================================================
"""

from ogs.validation import ValidationStatus

from ogs.smart_money.order_block.validation import (
    OrderBlockCandidateValidator,
)

from tests.factories import (
    make_bullish_order_block_candidate,
)


def test_create():

    validator = OrderBlockCandidateValidator()

    assert validator is not None


def test_none():

    validator = OrderBlockCandidateValidator()

    result = validator.validate(None)

    assert result.status == ValidationStatus.INVALID


def test_valid_candidate():

    validator = OrderBlockCandidateValidator()

    candidate = make_bullish_order_block_candidate()

    result = validator.validate(candidate)

    assert result.status == ValidationStatus.VALID