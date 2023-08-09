from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from api.v1.models.review import ReviewRatingEvent
from api.v1.models.user import UserEvent
from db.base_amqp import AmqpBroker
from models.base import Event, WorkerMessage
from services.amqp_broker_service import get_amqp_broker

router = APIRouter()


@router.post("/rating", summary="Оценка")
async def post_rating(
    review_rating_event: ReviewRatingEvent,
    amqp_broker: AmqpBroker = Depends(get_amqp_broker),
) -> Response:
    await amqp_broker.post(
        message_priority=review_rating_event.message_priority,
        message=WorkerMessage(
            transport_type=review_rating_event.transport_type,
            event=Event.REVIEW_RATED,
            body=review_rating_event.body,
        ),
    )
    return Response(status_code=HTTPStatus.OK)


@router.post(path="/user_registered", summary="Регистрация нового пользователя")
async def post_user_registered(
    user_event: UserEvent,
    amqp_broker: AmqpBroker = Depends(get_amqp_broker),
) -> Response:
    await amqp_broker.post(
        message_priority=user_event.message_priority,
        message=WorkerMessage(
            transport_type=user_event.transport_type,
            event=Event.USER_REGISTERED,
            body=user_event.body,
        ),
    )
    return Response(status_code=HTTPStatus.OK)
