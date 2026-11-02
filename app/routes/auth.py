from app.forms import RegisterForm, LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', form=RegisterForm())

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', form=LoginForm())