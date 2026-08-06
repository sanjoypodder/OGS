"""
Enumerations for Symbol module.
"""

from enum import Enum


class SymbolType(str, Enum):
    FOREX = "FOREX"
    CRYPTO = "CRYPTO"
    STOCK = "STOCK"
    INDEX = "INDEX"
    COMMODITY = "COMMODITY"
    FUTURES = "FUTURES"
    OPTION = "OPTION"
    ETF = "ETF"


class Exchange(str, Enum):
    NSE = "NSE"
    BSE = "BSE"
    MCX = "MCX"
    COMEX = "COMEX"
    CME = "CME"
    BINANCE = "BINANCE"
    BYBIT = "BYBIT"
    FOREX = "FOREX"
    UNKNOWN = "UNKNOWN"


class TradingStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"


class Currency(str, Enum):
    USD = "USD"
    INR = "INR"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    BTC = "BTC"
    USDT = "USDT"