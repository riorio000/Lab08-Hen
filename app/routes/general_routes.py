from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import LoginForm

general_blueprint = Blueprint('general', __name__)

@general_blueprint.route('/')
def home():
    return render_template('home.html')

@general_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Replace with your actual authentication logic
        username = form.username.data
        password = form.password.data
        # For example:
        if username == "admin" and password == "password":
            flash('Logged in successfully!', 'success')
            return redirect(url_for('general.index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)