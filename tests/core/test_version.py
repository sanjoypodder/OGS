from ogs.core.version import VERSION


def test_short_version() -> None:
    assert VERSION.short == "0.1.0"


def test_full_version() -> None:
    assert VERSION.full == "0.1.0-alpha.1"


def test_major() -> None:
    assert VERSION.major == 0


def test_minor() -> None:
    assert VERSION.minor == 1


def test_patch() -> None:
    assert VERSION.patch == 0


def test_stage() -> None:
    assert VERSION.stage == "alpha"


def test_build() -> None:
    assert VERSION.build == 1
