from ogs.core.application import Application
from ogs.core.logger import configure_logger

configure_logger()

app = Application()

print(app.application_state)

app.run()

print(app.application_state)

app.shutdown()

print(app.application_state)