from flask import render_template, Blueprint, redirect, url_for

# Create a blueprint for views
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/logout')
def logout():
    # Logic for logging out the user (e.g., clearing session)
    return redirect(url_for('views.home'))