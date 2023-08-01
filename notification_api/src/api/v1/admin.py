from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from api.v1.models.admin import AdminEvent
from brokers.base import Broker
from models.base import EventType, Message
from services import broker

router = APIRouter(prefix="/admin", tags=["Админ-панель"])


@router.post(
    path="/",
    summary="Событие из админ-панели",
)
async def post_admin_event(
    admin_event: AdminEvent,
    broker: Broker = Depends(broker.get_broker),  # noqa: WPS404, B008
) -> Response:
    message = Message(
        delivery_type=admin_event.delivery_type,
        event_type=EventType.ADMIN,
        body=admin_event.body,
    )
    await broker.post(priority=admin_event.priority, message=message)
    return Response(status_code=HTTPStatus.OK)
