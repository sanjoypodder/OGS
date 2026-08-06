"""
===========================================================

OGS Smart Money AI

Test Price Factory

Reusable immutable Price objects.

===========================================================
"""

from __future__ import annotations

from decimal import Decimal

from ogs.market import Price
from ogs.market import Symbol

from .symbol_factory import SymbolFactory


class PriceFactory:
    """
    Factory for immutable Price objects.

    Every price created through this factory automatically
    uses the correct Symbol.

    Examples
    --------

    price = PriceFactory.btc(100000)

    price = PriceFactory.gold(3400.25)

    price = PriceFactory.eurusd(1.17546)
    """

    # ======================================================
    # Generic
    # ======================================================

    @staticmethod
    def create(
        symbol: Symbol,
        value: int | float | str | Decimal,
    ) -> Price:
        """
        Generic price constructor.
        """

        return Price(
            symbol=symbol,
            value=Decimal(str(value)),
        )

    # ======================================================
    # BTC
    # ======================================================

    @staticmethod
    def btc(
        value: int | float | str | Decimal = 100000,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.btc(),
            value,
        )

    # ======================================================
    # ETH
    # ======================================================

    @staticmethod
    def eth(
        value: int | float | str | Decimal = 3000,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.eth(),
            value,
        )

    # ======================================================
    # GOLD
    # ======================================================

    @staticmethod
    def gold(
        value: int | float | str | Decimal = 3400,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.gold(),
            value,
        )

    # ======================================================
    # SILVER
    # ======================================================

    @staticmethod
    def silver(
        value: int | float | str | Decimal = 38,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.silver(),
            value,
        )

    # ======================================================
    # EURUSD
    # ======================================================

    @staticmethod
    def eurusd(
        value: int | float | str | Decimal = "1.17000",
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.eurusd(),
            value,
        )

    # ======================================================
    # GBPUSD
    # ======================================================

    @staticmethod
    def gbpusd(
        value: int | float | str | Decimal = "1.36000",
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.gbpusd(),
            value,
        )

    # ======================================================
    # USDJPY
    # ======================================================

    @staticmethod
    def usdjpy(
        value: int | float | str | Decimal = "150.000",
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.usdjpy(),
            value,
        )

    # ======================================================
    # US30
    # ======================================================

    @staticmethod
    def us30(
        value: int | float | str | Decimal = 45000,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.us30(),
            value,
        )

    # ======================================================
    # NAS100
    # ======================================================

    @staticmethod
    def nas100(
        value: int | float | str | Decimal = 23000,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.nas100(),
            value,
        )

    # ======================================================
    # SPX500
    # ======================================================

    @staticmethod
    def spx500(
        value: int | float | str | Decimal = 6500,
    ) -> Price:

        return PriceFactory.create(
            SymbolFactory.spx500(),
            value,
        )

    # ======================================================
    # Helpers
    # ======================================================

    @staticmethod
    def zero(symbol: Symbol | None = None) -> Price:
        """
        Zero price for any symbol.
        """

        symbol = symbol or SymbolFactory.default()

        return PriceFactory.create(
            symbol,
            Decimal("0"),
        )

    @staticmethod
    def one(symbol: Symbol | None = None) -> Price:
        """
        Price = 1
        """

        symbol = symbol or SymbolFactory.default()

        return PriceFactory.create(
            symbol,
            Decimal("1"),
        )

    @staticmethod
    def random(symbol: Symbol | None = None) -> Price:
        """
        Simple deterministic test value.

        Avoids randomness so tests remain reproducible.
        """

        symbol = symbol or SymbolFactory.default()

        return PriceFactory.create(
            symbol,
            Decimal("123.45"),
        )