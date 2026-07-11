from ogs.models import ApplicationState
from ogs.core.service_container import ServiceContainer
from ogs.core.shutdown import ShutdownManager
from ogs.core.logger import configure_logger

configure_logger()

print(ApplicationState.INITIALIZING)

container = ServiceContainer()

container.register("number", 100)

print(container.resolve("number"))

print(container.count)

shutdown = ShutdownManager()

shutdown.shutdown()