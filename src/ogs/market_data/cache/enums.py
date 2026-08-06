"""
OGS Smart Money AI

Cache Enums
"""

from enum import Enum


class CacheType(str, Enum):
    MEMORY = "MEMORY"
    REDIS = "REDIS"
    DISK = "DISK"
    HYBRID = "HYBRID"
    DISTRIBUTED = "DISTRIBUTED"
    UNKNOWN = "UNKNOWN"


class CacheStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    EVICTED = "EVICTED"
    DISABLED = "DISABLED"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"