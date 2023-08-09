from pydantic import BaseModel, EmailStr, Field, validator


class UserDetailsRequest(BaseModel):
    user_id: str = Field(..., title="Идентификатор пользователя")


class UserDetailsResponse(BaseModel):
    user_id: str = Field(..., title="Идентификатор пользователя")
    login: str = Field(..., title="Логин")
    email: str = Field(..., title="Почта")


class UsersDetailsRequest(BaseModel):
    name: str = Field(..., title="Название подписки")
