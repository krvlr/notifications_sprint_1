import datetime
import uuid

from pydantic import BaseModel, Field

from api.v1.models.base import Event


class ReviewRating(BaseModel):
    username: str
    review_id: uuid.UUID
    rating: int = Field(ge=0, le=10)
    updated_at: datetime.datetime


class ReviewRatingEvent(Event):
    body: ReviewRating
