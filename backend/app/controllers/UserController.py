from app import db, uploadconfig
from flask import request
from app.models.User import User
from app.res.response import get_success, bad_request, post_success, unauthorized, forbidden, not_found
from flask_jwt_extended import *

import datetime


def get():
    try:
        users = User.query.all()
        if users:
            data = formatarray(users)
            return get_success(data, "Data berhasil ditampilkan")
        return bad_request([], "User is empty!")
    except Exception as e:
        print(e)
        
def get_detail(id):
    one_user = User.query.get(id)
    users = User.query.all()
    if one_user:
        detail = formatarray(users)
        data = single_detail_object(one_user, detail)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "User tidak ditemukan")

def create():
    try:
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")
        active = request.form.get('active')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            return bad_request([], "Email sudah terdaftar")
        
        new_user = User(name=name, username=username, email=email, role=role, active=active)
        new_user.setPassword(password)
        db.session.add(new_user)
        db.session.commit()
        return post_success(new_user.name, "Sukses menambahkan User")
    except Exception as e:
        print(e)
        
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == '' or password == '':
        return bad_request([], "Email atau Password harus diisi")
    
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return bad_request([], "Username tidak terdaftar")
    
    if not user.checkPassword(password):
        return bad_request([], "Kombinasi Password salah")
    
    if user.active == "false":
        return bad_request([], "User di non-aktifkan")
    
    data = singleObject(user)
    
    expires = datetime.timedelta(days=10)
    expires_refresh = datetime.timedelta(days=10)
    
    token = create_access_token(identity=user.id, fresh=True, expires_delta= expires)
    refresh_token = create_refresh_token(identity=user.id, expires_delta=expires_refresh)
    
    return get_success({
        'data': data,
        'access_token': token,
        'refresh_token': refresh_token
    }, "Sukses Login!")
        
# Print out the json
def formatarray(data):
    array = []
    for i in data:
        array.append(singleObject(i))
        
    return array
        
def singleObject(data):
    data = {
        'id': data.id,
        'username': data.username,
        'name': data.name,
        'email': data.email,
        'role': data.role,
        'active': data.active
    }

    return data

def single_detail_object(user, detail):
    data = {
        'id': data.id,
        'username': data.username,
        'name': data.name,
        'email': data.email,
        'role': data.role,
        'active': data.active
    }
    
    return data