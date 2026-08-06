"""
===========================================================

OGS Smart Money AI

Order Block Validator Tests

===========================================================
"""

import pytest

from tests.factories import (
    make_bullish_order_block,
)

from ogs.smart_money.order_block import (
    OrderBlockValidator,
)


def test_valid():

    validator = OrderBlockValidator()

    validator.validate(
        make_bullish_order_block()
    )


def test_none():

    validator = OrderBlockValidator()

    with pytest.raises(ValueError):

        validator.validate(None)