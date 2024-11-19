from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import db, User, Class, Enrollment

# Create the Admin instance
admin = Admin(name='Admin Panel', template_mode='bootstrap4')

def setup_admin(app):
    # Attach Flask-Admin to the app
    admin.init_app(app)

    # Add models to the admin panel
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Class, db.session))
    admin.add_view(ModelView(Enrollment, db.session))