"""
===========================================================

OGS Smart Money AI

Market Symbol Registry

===========================================================
"""

from decimal import Decimal

from ogs.market.symbol import AssetClass, Symbol
from ogs.market.symbol_info import SymbolInfo

SYMBOLS: dict[Symbol, SymbolInfo] = {
    Symbol.XAUUSD: SymbolInfo(
        symbol=Symbol.XAUUSD,
        asset_class=AssetClass.METAL,
        tick_size=Decimal("0.01"),
        pip_size=Decimal("0.10"),
        price_precision=2,
        contract_size=100,
        display_name="Gold Spot",
        currency="USD",
    ),
    Symbol.BTCUSD: SymbolInfo(
        symbol=Symbol.BTCUSD,
        asset_class=AssetClass.CRYPTO,
        tick_size=Decimal("0.01"),
        pip_size=Decimal("1"),
        price_precision=2,
        contract_size=1,
        display_name="Bitcoin",
        currency="USD",
    ),
    Symbol.EURUSD: SymbolInfo(
        symbol=Symbol.EURUSD,
        asset_class=AssetClass.FOREX,
        tick_size=Decimal("0.00001"),
        pip_size=Decimal("0.00010"),
        price_precision=5,
        contract_size=100000,
        display_name="Euro / US Dollar",
        currency="USD",
    ),
}