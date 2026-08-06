"""
===========================================================

Module:
    symbol.py

Purpose:
    Market Symbol Definitions

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class AssetClass(StrEnum):
    """
    Supported asset classes.
    """

    FOREX = "FOREX"

    METAL = "METAL"

    CRYPTO = "CRYPTO"

    INDEX = "INDEX"

    STOCK = "STOCK"

    COMMODITY = "COMMODITY"


class Symbol(StrEnum):
    """
    Supported trading symbols.

    More symbols will be added in future releases.
    """

    # ======================
    # Metals
    # ======================

    XAUUSD = "XAUUSD"

    XAGUSD = "XAGUSD"

    # ======================
    # Crypto
    # ======================

    BTCUSD = "BTCUSD"

    ETHUSD = "ETHUSD"

    # ======================
    # Major Forex
    # ======================

    EURUSD = "EURUSD"

    GBPUSD = "GBPUSD"

    USDJPY = "USDJPY"

    USDCHF = "USDCHF"

    AUDUSD = "AUDUSD"

    NZDUSD = "NZDUSD"

    USDCAD = "USDCAD"

    # ======================
    # Index
    # ======================

    US30 = "US30"

    NAS100 = "NAS100"

    SPX500 = "SPX500"

    # -----------------------------

    @property
    def asset_class(self) -> AssetClass:
        """
        Return the asset class of the symbol.
        """

        mapping = {
            Symbol.XAUUSD: AssetClass.METAL,
            Symbol.XAGUSD: AssetClass.METAL,
            Symbol.BTCUSD: AssetClass.CRYPTO,
            Symbol.ETHUSD: AssetClass.CRYPTO,
            Symbol.EURUSD: AssetClass.FOREX,
            Symbol.GBPUSD: AssetClass.FOREX,
            Symbol.USDJPY: AssetClass.FOREX,
            Symbol.USDCHF: AssetClass.FOREX,
            Symbol.AUDUSD: AssetClass.FOREX,
            Symbol.NZDUSD: AssetClass.FOREX,
            Symbol.USDCAD: AssetClass.FOREX,
            Symbol.US30: AssetClass.INDEX,
            Symbol.NAS100: AssetClass.INDEX,
            Symbol.SPX500: AssetClass.INDEX,
        }

        return mapping[self]

    @property
    def is_forex(self) -> bool:
        return self.asset_class == AssetClass.FOREX

    @property
    def is_crypto(self) -> bool:
        return self.asset_class == AssetClass.CRYPTO

    @property
    def is_metal(self) -> bool:
        return self.asset_class == AssetClass.METAL

    @property
    def is_index(self) -> bool:
        return self.asset_class == AssetClass.INDEX
