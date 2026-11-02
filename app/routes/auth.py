from app.forms import RegisterForm, LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import Users
from app.utils import save_to_db, check_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # checking if user already exists in the database
        user_exists = Users.query.filter_by(email=email).first()
        
        if user_exists:
            flash('Email address already exists. Please use a different email.', 'danger')
            return redirect(url_for('auth.register'))
        else:
            # create new user
            try:
                new_user = Users(username=username, email=email, password=password)
                save_to_db(new_user)
                flash('Registration successful! You can now log in.', 'success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                print(f"Error occurred while saving user to database: {e}")
                flash('An error occurred while registering. Please try again.', 'danger')
                return redirect(url_for('auth.register'))

    return render_template('auth/register.html', form=RegisterForm())

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # check if user exists
        user = Users.query.filter_by(email=email).first()
        try:
            if user and check_hash(user.password, password):
                flash('Login successful!', 'success')
                print("success")
                return redirect(url_for('auth.register'))  # Redirect to a dashboard or home page after login
            else:
                print("not success")
                flash('Invalid email or password. Please try again.', 'danger')
        except Exception as e:
            print(f"Error occurred during login: {e}")
            flash('An error occurred during login. Please try again.', 'danger')


    return render_template('auth/login.html', form=LoginForm())