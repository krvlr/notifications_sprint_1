from flask import Blueprint

from api.v1.auth_handlers import auth_bp
from api.v1.oauth_handlers import oauth_bp
from api.v1.core import core_bp
from api.v1.role_handlers import role_bp
from api.v1.user_details_handlers import user_details_bp

api_auth_bp = Blueprint("api_auth", __name__, url_prefix="/api/v1")
api_auth_bp.register_blueprint(auth_bp)
api_auth_bp.register_blueprint(role_bp)
api_auth_bp.register_blueprint(oauth_bp)
api_auth_bp.register_blueprint(core_bp)
api_auth_bp.register_blueprint(user_details_bp)
