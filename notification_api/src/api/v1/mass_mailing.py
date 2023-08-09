from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from api.v1.models.mass_mailing import MassMailingEvent
from db.base_amqp import AmqpBroker
from models.base import Event, WorkerMessage
from services.amqp_broker_service import get_amqp_broker

router = APIRouter()


@router.post(path="/mass_mailing", summary="Массовая рассылка")
async def post_mass_mailing_event(
    mass_mailing_event: MassMailingEvent,
    amqp_broker: AmqpBroker = Depends(get_amqp_broker),
) -> Response:
    await amqp_broker.post(
        message_priority=mass_mailing_event.message_priority,
        message=WorkerMessage(
            transport_type=mass_mailing_event.transport_type,
            event=Event.MASS_MAILING,
            body=mass_mailing_event.body,
        ),
    )
    return Response(status_code=HTTPStatus.OK)
