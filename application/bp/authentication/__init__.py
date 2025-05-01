from flask import Blueprint, render_template, redirect, url_for, Response
from application.bp.authentication.forms import RegisterForm, LoginForm
from application.database import User
from flask_login import login_user, login_required, current_user, logout_user

authentication = Blueprint('authentication', __name__, template_folder='templates')


@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.create(form.email.data, form.password.data)
        user.save()
        return redirect(url_for('authentication.login'))
    return render_template('registration.html', form=form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Find user by email
        user = User.find_user_by_email(email)

        # Check if user exists
        if user is None:
            return Response("User Not Found\n" + render_template('login.html', form=form), 200)

        # Check if password is correct
        if not user.check_password(password):
            return Response("Password Incorrect\n" + render_template('login.html', form=form), 200)

        # User is valid, login and redirect to dashboard
        login_user(user)
        return redirect(url_for('authentication.dashboard'))

    return render_template('login.html', form=form)


@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage.homepage'))


@authentication.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=f"User ID: {current_user.id}")


@authentication.route('/user/<int:user_id>')
def user_by_id(user_id):
    user = User.find_user_by_id(user_id)
    return render_template('user.html', user=user)


@authentication.route('/users')
def users():
    user_records = User.all()
    return render_template('users.html', users=user_records)