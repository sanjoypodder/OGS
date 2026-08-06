from enum import Enum


class FlipZoneType(str, Enum):
    """
    Type of Flip Zone.
    """

    BULLISH = "Bullish"
    BEARISH = "Bearish"