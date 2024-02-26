from app import db
from datetime import datetime

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plu = db.Column(db.String(255), nullable=False)
    name = db.Column(db.Text, nullable=False)
    product_category_id = db.Column(db.Integer, nullable=False)
    active = db.Column(db.String(10), nullable=False)
    created_user = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    updated_user = db.Column(db.String(50), nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __repr__(self):
        return "<Products {}>".format(self.name)