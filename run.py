from app import create_app
from app.models import db, User, Class

app = create_app()
# with app.app_context():
#     # Create sample users
#     student = User(username="student1", password="hashed_password", role="student")
#     teacher = User(username="teacher1", password="hashed_password", role="teacher")
#     admin = User(username="admin1", password="hashed_password", role="admin")

#     # Create sample class
#     sample_class = Class(name="Math 101", max_capacity=30, teacher_id=2)

#     db.session.add_all([student, teacher, admin, sample_class])
#     db.session.commit()
# exit()

if __name__ == '__run__':
    app.run(host='127.0.0.1', port=5000, debug=True)
