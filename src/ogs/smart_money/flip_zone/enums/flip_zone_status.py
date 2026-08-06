from enum import Enum


class FlipZoneStatus(str, Enum):
    """
    Lifecycle state of a Flip Zone.
    """

    ACTIVE = "Active"

    TESTED = "Tested"

    CONFIRMED = "Confirmed"

    INVALIDATED = "Invalidated"