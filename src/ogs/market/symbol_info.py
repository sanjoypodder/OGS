"""
===========================================================

OGS Smart Money AI

Symbol Information

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ogs.market.symbol import AssetClass, Symbol


@dataclass(frozen=True, slots=True)
class SymbolInfo:
    """
    Immutable metadata describing a tradable symbol.
    """

    symbol: Symbol
    asset_class: AssetClass

    tick_size: Decimal

    pip_size: Decimal

    price_precision: int

    contract_size: int

    display_name: str

    currency: str

    def __str__(self) -> str:
        return self.display_name