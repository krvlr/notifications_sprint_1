from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from api.v1.models.admin import AdminEvent
from db.base_amqp import AmqpBroker
from models.base import Event, WorkerMessage
from services.amqp_broker_service import get_amqp_broker

router = APIRouter()


@router.post(path="/", summary="Панель администратора")
async def post_admin_event(
    admin_event: AdminEvent,
    amqp_broker: AmqpBroker = Depends(get_amqp_broker),
) -> Response:
    message = WorkerMessage(
        delivery_type=admin_event.delivery_type,
        event=Event.ADMIN,
        body=admin_event.body,
    )
    await amqp_broker.post(priority=admin_event.message_priority, message=message)
    return Response(status_code=HTTPStatus.OK)
