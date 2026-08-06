from __future__ import annotations

import pytest

from ogs.core.environment import EnvironmentManager


@pytest.fixture
def environment():
    """
    Return an EnvironmentManager instance.
    """

    return EnvironmentManager()
