from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify
from models.common import BaseResponse
from models.user_models import UserDetailsRequest, UserDetailsResponse, UsersDetailsRequest
from utils.exceptions import AccountUserDetailsException
from utils.rate_limit import limit_leaky_bucket
from utils.user_action import log_action
from services.user_details_service import get_user_details_service
from utils.common import get_data_from_body
from flask_jwt_extended import current_user, jwt_required, get_jwt
from utils.common import check_is_admin


user_details_bp = Blueprint("user", __name__)
user_details_service = get_user_details_service()


@user_details_bp.route("/users/user_details", methods=["POST"])
# @jwt_required()
# @check_is_admin
@swag_from("docs/users/user_details.yaml")
def user_details():
    try:
        body = get_data_from_body(UserDetailsRequest)
        data = user_details_service.get_user_details(
            # admin_id=current_user.id,
            # access_jti=get_jwt()["jti"],
            user_id=body.user_id
        )
        user_data = UserDetailsResponse(
            user_id=data["id"], login=data["login"], email=data["email"]
        ).dict()

        return jsonify(BaseResponse(data=user_data).dict()), HTTPStatus.OK
    except AccountUserDetailsException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@user_details_bp.route("/users/users_details", methods=["POST"])
# @jwt_required()
# @check_is_admin
@swag_from("docs/users/users_details.yaml")
def users_details():
    try:
        body = get_data_from_body(UsersDetailsRequest)
        data = user_details_service.get_users_details(
            # admin_id=current_user.id,
            # access_jti=get_jwt()["jti"],
            name=body.name
        )

        users_data = [
            UserDetailsResponse(user_id=user["id"], login=user["login"], email=user["email"]).dict()
            for user in data
        ]

        return jsonify(BaseResponse(data=users_data).dict()), HTTPStatus.OK
    except AccountUsersDetailsException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )
