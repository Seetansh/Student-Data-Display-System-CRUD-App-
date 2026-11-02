from flask import Flask, render_template, request, redirect, Blueprint

user_bp = Blueprint("user", __name__)

@user_bp.route('/dashboard')
def dashboard():
    
    return render_template('user/dashboard.html')