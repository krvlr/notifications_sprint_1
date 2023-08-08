from functools import lru_cache

from db.models.user import User, UserRole, Role
from db.token_storage_adapter import TokenStatus, TokenStorageAdapter, get_redis_adapter
from utils.exceptions import AccountUserDetailsException, AccountUsersDetailsException
from sqlalchemy import select
from db import alchemy


class UserDetailsService:
    def __init__(self, token_storage_adapter: TokenStorageAdapter):
        self.token_storage = token_storage_adapter

    def check_jwt_status(self, user_id: str, jti: str, ex: Exception):
        status = self.token_storage.get_status(user_id=user_id, jti=jti)

        if status == TokenStatus.NOT_FOUND:
            raise ex(error_message="Истек срок действия access токена.")
        elif status == TokenStatus.BLOCKED:
            raise ex(error_message="Данный access токен более не валиден.")

    def get_user_details(
        self,
        # admin_id: str,
        # access_jti: str,
        user_id: str,
    ) -> dict:
        # self.check_jwt_status(user_id=admin_id, jti=access_jti, ex=AccountUserDetailsException)

        user = User.query.filter_by(id=user_id, is_active=True).first()

        if not user:
            raise AccountUserDetailsException(
                error_message="Пользователя с таким user_id не существует."
            )

        return user.to_dict()

    def get_users_details(
        self,
        # admin_id: str,
        # access_jti: str,
        name: str,
    ) -> list[dict]:
        # self.check_jwt_status(user_id=admin_id, jti=access_jti, ex=AccountUsersDetailsException)

        query = (
            select(User)
            .join(UserRole, User.id == UserRole.user_id)
            .join(Role, Role.id == UserRole.role_id)
            .where(Role.name == name)
            .where(User.is_admin == False)
        )
        return [user.User.to_dict() for user in alchemy.session.execute(query)]


@lru_cache()
def get_user_details_service(token_storage_adapter: TokenStorageAdapter = get_redis_adapter()):
    return UserDetailsService(token_storage_adapter=token_storage_adapter)
