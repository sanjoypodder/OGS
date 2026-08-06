"""
===========================================================

OGS Smart Money AI

Immutable Price Value Object

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

from ogs.market.symbol import Symbol
from ogs.market.symbol_registry import SYMBOLS


@dataclass(frozen=True, slots=True)
class Price:
    """
    Immutable market price.
    """

    symbol: Symbol

    value: Decimal

    def __init__(
        self,
        symbol: Symbol,
        value: float | int | str | Decimal,
    ) -> None:

        info = SYMBOLS[symbol]

        precision = "1." + ("0" * info.price_precision)

        decimal_value = Decimal(str(value)).quantize(
            Decimal(precision),
            rounding=ROUND_HALF_UP,
        )

        object.__setattr__(self, "symbol", symbol)

        object.__setattr__(self, "value", decimal_value)

    def __str__(self) -> str:
        return str(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __add__(self, other: "Price") -> "Price":

        self._validate_symbol(other)

        return Price(
            self.symbol,
            self.value + other.value,
        )

    def __sub__(self, other: "Price") -> "Price":

        self._validate_symbol(other)

        return Price(
            self.symbol,
            self.value - other.value,
        )

    def __lt__(self, other: "Price") -> bool:

        self._validate_symbol(other)

        return self.value < other.value

    def __le__(self, other: "Price") -> bool:

        self._validate_symbol(other)

        return self.value <= other.value

    def __gt__(self, other: "Price") -> bool:

        self._validate_symbol(other)

        return self.value > other.value

    def __ge__(self, other: "Price") -> bool:

        self._validate_symbol(other)

        return self.value >= other.value

    @property
    def tick_size(self) -> Decimal:
        return SYMBOLS[self.symbol].tick_size

    @property
    def pip_size(self) -> Decimal:
        return SYMBOLS[self.symbol].pip_size

    @property
    def precision(self) -> int:
        return SYMBOLS[self.symbol].price_precision

    def _validate_symbol(
        self,
        other: "Price",
    ) -> None:

        if self.symbol != other.symbol:

            raise ValueError(
                "Cannot compare prices from different symbols."
            )