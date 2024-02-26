from app import app
from flask import request
from app.controllers import ProductCategory_Controller

# /api/admins
@app.route('/category', methods=['GET', 'POST'])
def get_post_category():
    if request.method == "GET":
        return ProductCategory_Controller.get()
    if request.method == "POST":
        return ProductCategory_Controller.create()
    
@app.route('/category/<id>', methods=['GET', 'PUT', 'DELETE'])
def detail_update_delete_category(id):
    if request.method == "GET":
        return ProductCategory_Controller.get_detail(id)
    # if request.method == "PUT":
    #     return ProductCategory_Controller