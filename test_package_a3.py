from ogs.core.logger import configure_logger

configure_logger()

from ogs.core.startup import StartupManager

startup = StartupManager()

startup.start()
