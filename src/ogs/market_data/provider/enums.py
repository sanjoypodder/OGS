"""
OGS Smart Money AI

Provider Enums
"""

from __future__ import annotations

from enum import Enum


class ProviderType(str, Enum):
    """
    Types of market data providers.
    """

    BROKER = "BROKER"

    EXCHANGE = "EXCHANGE"

    CRYPTO_EXCHANGE = "CRYPTO_EXCHANGE"

    DATA_VENDOR = "DATA_VENDOR"

    DATABASE = "DATABASE"

    CSV = "CSV"

    FILE = "FILE"

    SIMULATION = "SIMULATION"

    BACKTEST = "BACKTEST"

    UNKNOWN = "UNKNOWN"


class ConnectionStatus(str, Enum):
    """
    Current provider connection state.
    """

    CONNECTED = "CONNECTED"

    DISCONNECTED = "DISCONNECTED"

    CONNECTING = "CONNECTING"

    RECONNECTING = "RECONNECTING"

    ERROR = "ERROR"

    UNKNOWN = "UNKNOWN"