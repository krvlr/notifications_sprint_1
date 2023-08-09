import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import events, mass_mailing, core
from core.config import project_settings
from core.logger import LOGGER_CONFIG
from services import amqp_broker_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=project_settings.project_name,
    docs_url="/api/v1/openapi",
    openapi_url="/api/v1/openapi.json",
    default_response_class=ORJSONResponse,
)

app.include_router(core.router, prefix="/api/v1", tags=["core"])
app.include_router(events.router, prefix="/api/v1/events", tags=["События"])
app.include_router(mass_mailing.router, prefix="/api/v1/mass", tags=["Массовая рассылка"])


@app.on_event("startup")
async def startup():
    logger.info("startup")
    await amqp_broker_service.connect()


@app.on_event("shutdown")
async def shutdown():
    logger.info("shutdown")
    await amqp_broker_service.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_config=LOGGER_CONFIG)
