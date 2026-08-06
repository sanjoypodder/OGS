"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Validator Tests

===========================================================
"""

import pytest

from tests.factories import (
    make_candle,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    LiquiditySweepValidator,
    SweepDirection,
    SweepStatus,
)


def test_valid(sample_sweep):

    validator = LiquiditySweepValidator()

    validator.validate(sample_sweep)


def test_none():

    validator = LiquiditySweepValidator()

    with pytest.raises(ValueError):

        validator.validate(None)


def test_none_pool():

    validator = LiquiditySweepValidator()

    sweep = LiquiditySweep(
        liquidity_pool=None,
        sweep_candle=make_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    with pytest.raises(ValueError):

        validator.validate(sweep)