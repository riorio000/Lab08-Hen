from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .models import db, bcrypt
from .routes.admin_routes import setup_admin
from .routes.general_routes import general_blueprint
from .views import views
import os

def create_app():
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
                static_folder=os.path.join(os.path.dirname(__file__), 'static'))  # Explicitly set static folder
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "views.login"  

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register routes
    from .routes.student_routes import student_blueprint
    from .routes.teacher_routes import teacher_blueprint

    app.register_blueprint(student_blueprint)
    app.register_blueprint(teacher_blueprint)
    app.register_blueprint(general_blueprint)
    app.register_blueprint(views)

    # Setup Flask-Admin
    setup_admin(app)

    return app