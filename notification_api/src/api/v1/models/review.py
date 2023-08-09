import datetime
import uuid

from pydantic import BaseModel, Field

from api.v1.models.base import Event


class ReviewRating(BaseModel):
    user_id: uuid.UUID
    review_id: uuid.UUID
    rating: int = Field(ge=0, le=10)
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ReviewRatingEvent(Event):
    body: ReviewRating
