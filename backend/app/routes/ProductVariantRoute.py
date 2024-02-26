from app import app
from flask import request
from app.controllers import ProductVariant_Controller

# /api/admins
@app.route('/variants', methods=['GET', 'POST'])
def get_post_variant():
    if request.method == "GET":
        return ProductVariant_Controller.get()
    if request.method == "POST":
        return ProductVariant_Controller.create()
    
@app.route('/variant/<id>', methods=['GET', 'PUT', 'DELETE'])
def detail_update_delete_variant(id):
    if request.method == "GET":
        return ProductVariant_Controller.get_detail(id)
    if request.method == "PUT":
        return ProductVariant_Controller.update(id)
    if request.method == "DELETE":
        return ProductVariant_Controller.delete(id)