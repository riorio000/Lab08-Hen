from flask import render_template, Blueprint, redirect, url_for

# Create a blueprint for views
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/register')
def register():
    return render_template('register.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/logout')
def logout():
    # Logic for logging out the user (e.g., clearing session)
    return redirect(url_for('views.home'))

@views.route('/student_portal')
def student_portal(): # Student portal
    return render_template('student_portal.html')