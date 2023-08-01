import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import project_settings, logger_settings
from core.logger import LOGGER_CONFIG
from api.v1 import events, admin
from services import broker

app = FastAPI(
    title=project_settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)
app.include_router(events.router)
app.include_router(admin.router)


@app.on_event("startup")
async def startup():
    await broker.connect()


@app.on_event("shutdown")
async def shutdown():
    await broker.disconnect()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=LOGGER_CONFIG,
        debug=logger_settings.debug,
    )
