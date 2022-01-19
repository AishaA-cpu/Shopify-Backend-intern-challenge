from app import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime)
    #inventory = db.relationship("Inventory", back_populates="shipments")
    