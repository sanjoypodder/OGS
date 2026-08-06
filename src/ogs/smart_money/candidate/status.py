"""
===========================================================

OGS Smart Money AI

Candidate Status

===========================================================
"""

from enum import StrEnum


class CandidateStatus(StrEnum):
    """
    Generic candidate lifecycle.
    """

    DETECTED = "DETECTED"

    VALIDATED = "VALIDATED"

    REJECTED = "REJECTED"