from app import app
from flask import request
from app.controllers import ProductsController

# /api/admins
@app.route('/products', methods=['GET', 'POST'])
def get_post_product():
    if request.method == "GET":
        return ProductsController.get()
    if request.method == "POST":
        return ProductsController.create()
    
@app.route('/product/<id>', methods=['GET', 'PUT', 'DELETE'])
def detail_update_delete_product(id):
    if request.method == "GET":
        return ProductsController.get_detail(id)
    if request.method == "PUT":
        return ProductsController.update(id)
    if request.method == "DELETE":
        return ProductsController.delete(id)