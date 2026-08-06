"""
OGS Smart Money AI
Tick Enumerations
"""

from enum import Enum


class TickType(str, Enum):
    """
    Type of market tick.
    """

    BID = "BID"
    ASK = "ASK"
    LAST = "LAST"
    MID = "MID"


class ProviderType(str, Enum):
    """
    Supported market data providers.
    """

    FYERS = "FYERS"

    BINANCE = "BINANCE"

    BYBIT = "BYBIT"

    MT5 = "MT5"

    TRADINGVIEW = "TRADINGVIEW"

    UPSTOX = "UPSTOX"

    ZERODHA = "ZERODHA"

    CSV = "CSV"

    BACKTEST = "BACKTEST"

    SIMULATION = "SIMULATION"

    UNKNOWN = "UNKNOWN"