import pytest

from ogs.smart_money.breaker import (
    BreakerBlockValidator,
)

from tests.factories.breaker_factory import (
    make_bullish_breaker,
)


def test_valid():
    breaker = make_bullish_breaker()

    BreakerBlockValidator.validate(breaker)


def test_invalid_size():
    breaker = make_bullish_breaker()

    object.__setattr__(breaker, "size", -1)

    with pytest.raises(ValueError):
        BreakerBlockValidator.validate(breaker)