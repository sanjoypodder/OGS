from tests.factories import (
    make_bullish_fair_value_gap,
)

from ogs.smart_money.fair_value_gap import (
    FairValueGapValidator,
)


def test_validator():

    validator = FairValueGapValidator()

    assert validator.validate(
        make_bullish_fair_value_gap()
    )