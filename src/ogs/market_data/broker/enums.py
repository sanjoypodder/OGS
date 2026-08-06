"""
OGS Smart Money AI

Broker Enums
"""

from enum import Enum


class BrokerStatus(Enum):
    """
    Broker operational status.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"
    CLOSED = "CLOSED"
    UNKNOWN = "UNKNOWN"


class MarketType(Enum):
    """
    Supported market types.
    """

    EQUITY = "EQUITY"
    FUTURES = "FUTURES"
    OPTIONS = "OPTIONS"
    FOREX = "FOREX"
    CRYPTO = "CRYPTO"
    COMMODITY = "COMMODITY"
    BONDS = "BONDS"