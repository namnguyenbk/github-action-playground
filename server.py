from sanic import Sanic
import sentry_sdk
from sanic.response import text
from sentry_sdk.integrations.sanic import SanicIntegration

app = Sanic("MyHelloWorldApp")


@app.get("/hello")
async def hello_world(request):
    return text("Hello, world.")


sentry_sdk.init(
    "",
    environment='development',
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    integrations=[
        SanicIntegration()
    ],
    traces_sample_rate=1.0,
)
