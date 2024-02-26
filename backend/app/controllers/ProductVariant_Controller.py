import os
import uuid
from app import app, db, uploadconfig
from flask import Flask, request, jsonify
from app.models.Product_Variant import Product_Variant
from werkzeug.utils import secure_filename
from app.res.response import get_success, bad_request, post_success, delete_success

def get():
    products = Product_Variant.query.all()
    if products:
        data = formatarray(products)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Varian Produk tidak ditemukan")

def get_detail(id):
    one_product = Product_Variant.query.get(id)
    products = Product_Variant.query.all()
    if one_product:
        detail = formatarray(products)
        data = single_detail_object(one_product, detail)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Variant tidak ditemukan")

def create():
    products = Product_Variant.query.all()
    if products:
        last_item = products[-1]
        variant_id = last_item.id + 1
    else:
        variant_id = 1
        
    if 'image_location' not in request.files:
        return bad_request([], "Field gambar tidak tersedia. Input data harus beserta gambar")
    
    name = request.form.get('name')
    product_id = int(request.form.get('product_id'))
    product_code = "PDCT"
    code = f"{product_code}{product_id:07d}{variant_id:04d}"
    qty = request.form.get('qty')
    price = request.form.get('price')
    active = request.form.get('active')
    created_user = "Operator"
    updated_user = "Operator"
    file = request.files["image_location"]
    
    if file.filename == '':
        new_variant = Product_Variant(product_id=product_id, code=code, name=name, qty=qty, price=price, active=active, created_user=created_user, updated_user=updated_user)
        db.session.add(new_variant)
        db.session.commit()
        return post_success(new_variant.name, "Sukses menambahkan data")
    
    if file and uploadconfig.allowed_file(file.filename):
        uid = uuid.uuid4()
        filename = secure_filename(file.filename)
        renamefile = "Flask-"+str(uid)+filename
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/product_variant', renamefile))
        
        new_variant = Product_Variant(product_id=product_id, image_location=renamefile, code=code, name=name, qty=qty, price=price, active=active, created_user=created_user, updated_user=updated_user)
        db.session.add(new_variant)
        db.session.commit()
        return post_success(new_variant.name, "Sukses menambahkan data")
    
def update(id):
    variant = Product_Variant.query.get(id)
    if variant:
        name = request.form.get('name')
        product_id = request.form.get('product_id')
        product_code = "PDCT"
        code = f"{product_code}{product_id:07d}{variant.id:04d}"
        qty = request.form.get('qty')
        price = request.form.get('price')
        active = request.form.get('active')
        updated_user = "Operator"
        file = request.files["image_location"]
        
        if 'image_location' not in request.files:
            return bad_request([], "Field gambar tidak tersedia. Input data harus beserta gambar")
        
        if file.filename == '':
            variant.name = name
            variant.product_id = product_id
            variant.code = code
            variant.qty = qty
            variant.price = price
            variant.active = active
            variant.update_user = updated_user
            variant.image_location = ""
            db.session.commit()
            return post_success(variant.id, "Sukses mengedit data")
        
        if file and uploadconfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename
            
            # For remove previous image
            if variant.image_location is not "":
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'] + '/product_variant', variant.image_location))
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/product_variant', renamefile))
            
            variant.name = name
            variant.product_id = product_id
            variant.code = code
            variant.qty = qty
            variant.price = price
            variant.active = active
            variant.update_user = updated_user
            variant.image_location = renamefile
            db.session.commit()
            return post_success(variant.id, "Sukses mengedit data")
        
    return bad_request([], "Variant tidak ditemukan")    
        
def delete(id):
    one_variant = Product_Variant.query.get(id)
    if one_variant:
        db.session.delete(one_variant)
        db.session.commit()
        return delete_success(one_variant.id, "Variant berhasil di hapus")
    return bad_request([], "Variant tidak ditemukan")

# Print out the json
def formatarray(data):
    array = []
    for i in data:
        array.append(singleObject(i))
        
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'product_id': data.product_id,
        'code': data.code,
        'name': data.name,
        'image_location': data.image_location,
        'qty': data.qty,
        'price': data.price,
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
        'product_id': data.product_id,
        'code': data.code,
        'name': data.name,
        'image_location': data.image_location,
        'qty': data.qty,
        'price': data.price,
        'active': data.active,
        'created_user': data.created_user,
        'created_date': data.created_date,
        'updated_user': data.updated_user,
        'updated_date': data.updated_date
    }
    
    return object