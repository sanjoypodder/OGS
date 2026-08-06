from decimal import Decimal

import pytest

from ogs.smart_money.flip_zone.domain.flip_zone import FlipZone
from ogs.smart_money.flip_zone.validator.flip_zone_validator import (
    FlipZoneValidator,
)


def test_valid_zone():

    zone = FlipZone(
        upper_price=Decimal("110"),
        lower_price=Decimal("100"),
        flip_price=Decimal("105"),
        originating_bos_id="bos1",
        originating_swing_id="sw1",
    )

    assert FlipZoneValidator.is_valid(zone)


def test_invalid_price():

    zone = FlipZone(
        upper_price=Decimal("90"),
        lower_price=Decimal("100"),
        flip_price=Decimal("95"),
        originating_bos_id="bos1",
        originating_swing_id="sw1",
    )

    with pytest.raises(ValueError):
        FlipZoneValidator.validate(zone)