from __future__ import annotations

import pytest

from ogs.core.application import Application


@pytest.fixture
def application():
    """
    Return a fresh Application instance.
    """

    return Application()
