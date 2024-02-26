import os
import uuid
from app import app, db, uploadconfig
from flask import Flask, request, jsonify
from app.models.Products import Products
from app.res.response import get_success, bad_request, post_success, delete_success

def get():
    products = Products.query.all()
    if products:
        data = formatarray(products)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Produk tidak ditemukan")

def get_detail(id):
    one_product = Products.query.get(id)
    products = Products.query.all()
    if one_product:
        detail = formatarray(products)
        data = single_detail_object(one_product, detail)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Produk tidak ditemukan")

def create():
    try:
        products = Products.query.all()
        if products:
            last_product = products[-1]
            product_id = last_product.id + 1
        else:
            product_id = 1

        product_code = "PDCT"
        plu = f"{product_code}{product_id:07d}"
        name = request.form.get("name")
        product_category_id = request.form.get("product_category_id")
        active = request.form.get('active')
        created_user = "Operator"
        updated_user = "Operator"
            
        new_product = Products(plu=plu, name=name, product_category_id=product_category_id, active=active, created_user=created_user, updated_user=updated_user)
        db.session.add(new_product)
        db.session.commit()
        return post_success(new_product.plu, "Sukses menambahkan Produk")
    except Exception as e:
        print(e)
        
def update(id):
    one_product = Products.query.get(id)
    if one_product:
        name = request.form.get('name')
        product_category_id = request.form.get("product_category_id")
        active = request.form.get('active')
        updated_user = "Operator"
        
        one_product.name = name
        one_product.product_category_id = product_category_id
        one_product.active = active
        one_product.updated_user = updated_user
        
        db.session.commit()
        return post_success(one_product.id, "Sukses mengedit data")
    
def delete(id):
    one_product = Products.query.get(id)
    if one_product:
        db.session.delete(one_product)
        db.session.commit()
        return delete_success(one_product.id, "Produk berhasil di hapus")
    return bad_request([], "Produk tidak ditemukan")

# Print out the json
def formatarray(data):
    array = []
    for i in data:
        array.append(singleObject(i))
        
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'plu': data.plu,
        'name': data.name,
        'product_category_id': data.product_category_id,
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
        'plu': data.plu,
        'name': data.name,
        'product_category_id': data.product_category_id,
        'active': data.active,
        'created_user': data.created_user,
        'created_date': data.created_date,
        'updated_user': data.updated_user,
        'updated_date': data.updated_date
    }
    
    return object