from app import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    total_quantity = db.Column(db.Integer)
