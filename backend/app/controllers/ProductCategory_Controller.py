import os
import uuid
from app import app, db, uploadconfig
from flask import Flask, request, jsonify
from app.models.Product_Category import Product_Category
from app.res.response import get_success, bad_request, post_success, delete_success

def get():
    products = Product_Category.query.all()
    if products:
        data = formatarray(products)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Kategori Barang tidak ditemukan")

def get_detail(id):
    one_category = Product_Category.query.get(id)
    products = Product_Category.query.all()
    if one_category:
        detail = formatarray(products)
        data = single_detail_object(one_category, detail)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Kategori Barang tidak ditemukan")

def create():
    try:
        name = request.form.get('name')
        active = request.form.get('active')
        created_user = "Operator"
        updated_user = "Operator"
        
        new_category = Product_Category(name=name, active=active, created_user=created_user, updated_user=updated_user)
        db.session.add(new_category)
        db.session.commit()
        return post_success(new_category.name, "Sukses menambahkan data!")
    except Exception as e:
        print(e)
        
def update(id):
    one_category = Product_Category.query.get(id)
    if one_category:
        name = request.form.get('name')
        active = request.form.get('active')
        updated_user = "Operator"
        
        one_category.name = name
        one_category.active = active
        one_category.updated_user = updated_user
        
        db.session.commit()
        return post_success(one_category.id, "Sukses mengedit data")
    
def delete(id):
    one_category = Product_Category.query.get(id)
    if one_category:
        db.session.delete(one_category)
        db.session.commit()
        return delete_success(one_category.id, "Kategori berhasil di hapus")
    return bad_request([], "Kategori tidak ditemukan")

# Print out the json
def formatarray(data):
    array = []
    for i in data:
        array.append(singleObject(i))
        
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'active': data.active,
        'created_user': data.created_user,
        'created_date': data.created_date,
        'updated_user': data.updated_user,
        'updated_date': data.updated_date
    }

    return data

def single_detail_object(data, detail):
    object = {
        'id': data.id,
        'name': data.name,
        'active': data.active,
        'created_user': data.created_user,
        'created_date': data.created_date,
        'updated_user': data.updated_user,
        'updated_date': data.updated_date
    }
    
    return object