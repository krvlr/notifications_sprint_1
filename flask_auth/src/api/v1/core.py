from http import HTTPStatus

from flask import Blueprint, jsonify
from models.common import BaseResponse
from flasgger import swag_from


core_bp = Blueprint("core", __name__)


@core_bp.route("/health", methods=["GET"])
@swag_from("docs/core/health.yaml")
def health():
    return jsonify(BaseResponse().dict()), HTTPStatus.OK
