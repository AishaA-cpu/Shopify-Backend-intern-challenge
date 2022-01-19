from app import db
# Shipments has a one to many relationship with inventories 
# also inherits from the SQLA base class

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime)
    
    
