from pydantic import BaseModel


class Task(BaseModel):
    template: str
    users: list[str]
