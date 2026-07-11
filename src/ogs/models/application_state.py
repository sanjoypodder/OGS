"""
===========================================================

Module:
    application_state.py

Purpose:
    Defines the lifecycle states of the OGS application.

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class ApplicationState(StrEnum):
    """
    Represents the lifecycle state of the application.
    """

    STOPPED = "STOPPED"

    INITIALIZING = "INITIALIZING"

    RUNNING = "RUNNING"

    SHUTTING_DOWN = "SHUTTING_DOWN"

    ERROR = "ERROR"