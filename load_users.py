import csv
from app import db, create_app  # Import your Flask app and database instance
from app.models import User  # Import your User model
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Create app context
app = create_app()
with app.app_context():
    # Open the CSV file
    with open('users.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            # Hash the password before saving
            hashed_password = bcrypt.generate_password_hash(row['password']).decode('utf-8')

            # Create a new User object
            user = User(
                id=row['id'],
                username=row['username'],
                password=hashed_password,
                role=row['role']
            )

            # Add the user to the session
            db.session.add(user)

    # Commit the transaction
    db.session.commit()
    print("Users loaded into the database successfully!")