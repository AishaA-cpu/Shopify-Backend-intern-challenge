from app import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)