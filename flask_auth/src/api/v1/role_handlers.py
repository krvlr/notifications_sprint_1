from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify
from flask_jwt_extended import current_user, jwt_required, get_jwt
from models.common import BaseResponse
from models.role_models import (
    AddUserRoleRequest,
    CheckUserRoleRequest,
    CreateRoleRequest,
    DeleteUserRoleRequest,
    ModifiedRoleRequest,
    PaginatorRequest,
    RoleResponse,
)
from services.role_service import get_role_service
from utils.common import check_is_admin, get_data_from_body, get_data_from_params, set_jwt_in_cookie
from utils.exceptions import (
    AccountAddUserRoleException,
    AccountCheckUserRoleException,
    AccountCreateRoleException,
    AccountDeleteRoleException,
    AccountDeleteUserRoleException,
    AccountModifiedRoleException,
    AccountRoleDetailsException,
    AccountRolesDetailsException,
)

role_bp = Blueprint("roles", __name__)
role_service = get_role_service()


@role_bp.route("/roles/create_role", methods=["POST"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/create_role.yaml")
def create_role():
    try:
        body = get_data_from_body(CreateRoleRequest)

        role_data = RoleResponse(
            **role_service.create_role(
                admin_id=current_user.id,
                access_jti=get_jwt()["jti"],
                name=body.name,
                description=body.description,
            )
        ).dict()

        return (
            jsonify(BaseResponse(success=True, data=role_data).dict()),
            HTTPStatus.OK,
        )
    except AccountCreateRoleException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/role_details/<name>", methods=["GET"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/role_details.yaml")
def role_details(name: str):
    try:
        role_data = RoleResponse(
            **role_service.role_details(
                admin_id=current_user.id, access_jti=get_jwt()["jti"], name=name
            )
        ).dict()

        return (
            jsonify(BaseResponse(success=True, data=role_data).dict()),
            HTTPStatus.OK,
        )
    except AccountRoleDetailsException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/roles_details", methods=["GET"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/roles_details.yaml")
def roles_details():
    try:
        roles_data = [
            RoleResponse(**role_data).dict()
            for role_data in role_service.roles_details(
                admin_id=current_user.id, access_jti=get_jwt()["jti"]
            )
        ]

        return (
            jsonify(BaseResponse(success=True, data=roles_data).dict()),
            HTTPStatus.OK,
        )
    except AccountRolesDetailsException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/delete_role/<name>", methods=["DELETE"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/delete_role.yaml")
def delete_role(name: str):
    try:
        role_service.delete_role(admin_id=current_user.id, access_jti=get_jwt()["jti"], name=name)

        return (
            jsonify(BaseResponse(success=True).dict()),
            HTTPStatus.OK,
        )
    except AccountDeleteRoleException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/modified_role/<name>", methods=["PUT"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/modified_role.yaml")
def modified_role(name: str):
    try:
        body = get_data_from_body(ModifiedRoleRequest)

        role_data = RoleResponse(
            **role_service.modified_role(
                admin_id=current_user.id,
                access_jti=get_jwt()["jti"],
                name=name,
                new_name=body.new_name,
                new_description=body.new_description,
            )
        ).dict()

        return (
            jsonify(BaseResponse(success=True, data=role_data).dict()),
            HTTPStatus.OK,
        )
    except AccountModifiedRoleException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/add_user_role/<name>", methods=["POST"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/add_user_role.yaml")
def add_user_role(name: str):
    try:
        body = get_data_from_body(AddUserRoleRequest)

        role_service.add_user_role(
            admin_id=current_user.id,
            access_jti=get_jwt()["jti"],
            user_id=body.user_id,
            name=name,
        )

        return (
            jsonify(BaseResponse(success=True).dict()),
            HTTPStatus.OK,
        )
    except AccountAddUserRoleException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/delete_user_role/<name>", methods=["DELETE"])
@jwt_required()
@check_is_admin
@swag_from("docs/roles/delete_user_role.yaml")
def delete_user_role(name: str):
    try:
        body = get_data_from_body(DeleteUserRoleRequest)

        role_service.delete_user_role(
            admin_id=current_user.id,
            access_jti=get_jwt()["jti"],
            user_id=body.user_id,
            name=name,
        )

        return (
            jsonify(BaseResponse(success=True).dict()),
            HTTPStatus.OK,
        )
    except AccountDeleteUserRoleException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )


@role_bp.route("/roles/check_user_role/<name>", methods=["GET"])
@jwt_required()
@swag_from("docs/roles/check_user_role.yaml")
def check_user_role(name: str):
    try:
        body = get_data_from_body(CheckUserRoleRequest)

        role_service.check_user_role(
            admin_id=current_user.id,
            access_jti=get_jwt()["jti"],
            user_id=body.user_id,
            name=name,
        )

        return (
            jsonify(BaseResponse(success=True).dict()),
            HTTPStatus.OK,
        )
    except AccountCheckUserRoleException as ex:
        return (
            jsonify(BaseResponse(success=False, error=ex.error_message).dict()),
            HTTPStatus.BAD_REQUEST,
        )
