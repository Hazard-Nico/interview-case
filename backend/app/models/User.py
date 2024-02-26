from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(250), nullable=False)
    active = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return "<User {}>".format(self.name)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)
        
    def checkPassword(self, password):
        return check_password_hash(self.password, password)