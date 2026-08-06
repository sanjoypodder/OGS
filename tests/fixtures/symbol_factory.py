"""
===========================================================

OGS Smart Money AI

Test Symbol Factory

Reusable Symbol objects for unit tests.

===========================================================
"""

from __future__ import annotations

from ogs.market import Symbol


class SymbolFactory:
    """
    Factory for creating market symbols.

    Examples
    --------
    symbol = SymbolFactory.btc()

    symbol = SymbolFactory.gold()

    symbol = SymbolFactory.forex()
    """

    @staticmethod
    def btc() -> Symbol:
        """
        Bitcoin
        """
        return Symbol.BTCUSD

    @staticmethod
    def eth() -> Symbol:
        """
        Ethereum
        """
        return Symbol.ETHUSD

    @staticmethod
    def gold() -> Symbol:
        """
        Gold
        """
        return Symbol.XAUUSD

    @staticmethod
    def silver() -> Symbol:
        """
        Silver
        """
        return Symbol.XAGUSD

    @staticmethod
    def eurusd() -> Symbol:
        """
        EURUSD
        """
        return Symbol.EURUSD

    @staticmethod
    def gbpusd() -> Symbol:
        """
        GBPUSD
        """
        return Symbol.GBPUSD

    @staticmethod
    def usdjpy() -> Symbol:
        """
        USDJPY
        """
        return Symbol.USDJPY

    @staticmethod
    def usdchf() -> Symbol:
        """
        USDCHF
        """
        return Symbol.USDCHF

    @staticmethod
    def audusd() -> Symbol:
        """
        AUDUSD
        """
        return Symbol.AUDUSD

    @staticmethod
    def nzdusd() -> Symbol:
        """
        NZDUSD
        """
        return Symbol.NZDUSD

    @staticmethod
    def usdcad() -> Symbol:
        """
        USDCAD
        """
        return Symbol.USDCAD

    @staticmethod
    def us30() -> Symbol:
        """
        US30
        """
        return Symbol.US30

    @staticmethod
    def nas100() -> Symbol:
        """
        NAS100
        """
        return Symbol.NAS100

    @staticmethod
    def spx500() -> Symbol:
        """
        SPX500
        """
        return Symbol.SPX500

    @staticmethod
    def default() -> Symbol:
        """
        Default testing symbol.

        BTCUSD is used throughout the project.
        """
        return Symbol.BTCUSD

    @staticmethod
    def all_symbols() -> list[Symbol]:
        """
        Return every supported symbol.
        """
        return list(Symbol)