from app import db
from datetime import datetime

class Transaction_Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_id = db.Column(db.Integer, nullable=False)
    product_variant_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Integer, nullable=False)
    active = db.Column(db.String(10), nullable=False)
    created_user = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    updated_user = db.Column(db.String(50), nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __repr__(self):
        return "<Transaction_Detail {}>".format(self.name)