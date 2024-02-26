from flask import Flask, jsonify
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# app instance
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'xxxxxxxxxx'
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app.models import User, Transaction, Transaction_Detail, Product_Category, Product_Variant, Products
from app.routes import ProductCategoryRoute, ProductRoute, ProductVariantRoute, UserRoute