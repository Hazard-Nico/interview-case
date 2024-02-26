from app import app
from flask import request
from app.controllers import UserController

@app.route('/users', methods=["GET"])
def get_users():
    return UserController.get()

@app.route('/createuser', methods=["POST"])
def creates_user():
    return UserController.create()

@app.route("/login", methods=["POST"])
def logins():
    return UserController.login()