import os

from flask import Flask
from app.controllers.auth_controller import auth
from app.common import response
from .config import config
from flask_security import Security,SQLAlchemySessionUserDatastore
from app.models.auth import User, Role ,user_datastore

from app.common.database import db_session
from app.common.cache import  cache



project_dir = os.path.dirname(os.path.abspath(__file__))



def create_app():
    print(__name__)

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'super-secret'
    


    register_security(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_cache(app):
    """Register Flask cache."""
    cache.init_app(app)
    return None


def register_security(app):
    security = Security(app, user_datastore)
    def unauth_handler():
        return response.error_response("未登录",401)
    security.unauthorized_handler(unauth_handler);

    
        
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()


# def register_extensions(app):
#     """Register Flask extensions."""
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#     return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(auth)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(401)
    def internal_error(error):
        return response.error_response("未登录",401)
    
    @app.login_manager.unauthorized_handler
    def unauth_handler():
        return response.error_response("未登录",401)

    @app.errorhandler(404)
    def api_not_found(error):
        return response.error_response("资源未发现", 404)

    @app.errorhandler(500)
    def server_error(error):
        return response.error_response("服务器错误", 500)

    return None
