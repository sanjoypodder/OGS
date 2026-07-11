"""
===========================================================

OGS Smart Money AI

Application Entry Point

Author:
    Om Ganapati Solution

===========================================================
"""

from ogs.core.application import Application


def main() -> None:
    """
    OGS Entry Point.
    """

    application = Application()

    application.run()

    application.shutdown()


if __name__ == "__main__":
    main()
