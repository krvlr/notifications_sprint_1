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
    message = WorkerMessage(
        delivery_type=review_rating_event.delivery_type,
        event=Event.REVIEW_RATED,
        body=review_rating_event.body,
    )
    await amqp_broker.post(
        priority=review_rating_event.message_priority,
        message=message,
    )
    return Response(status_code=HTTPStatus.OK)


@router.post(path="/user_registered", summary="Регистрация нового пользователя")
async def post_user_registered(
    user_event: UserEvent,
    amqp_broker: AmqpBroker = Depends(get_amqp_broker),
) -> Response:
    message = WorkerMessage(
        delivery_type=user_event.delivery_type,
        event=Event.USER_REGISTERED,
        body=user_event.body,
    )
    await amqp_broker.post(priority=user_event.message_priority, message=message)
    return Response(status_code=HTTPStatus.OK)
