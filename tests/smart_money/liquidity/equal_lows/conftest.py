"""
===========================================================

OGS Smart Money AI

Equal Low Test Fixtures

===========================================================
"""

from __future__ import annotations

from decimal import Decimal

import pytest

from tests.factories import make_swing_low

from ogs.smart_money.liquidity.equal_lows import (
    EqualLow,
    EqualLowType,
)


@pytest.fixture
def sample_equal_low():

    return EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=make_swing_low(index=8),
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )