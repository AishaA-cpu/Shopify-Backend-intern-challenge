from app import db


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    shipment_id = db.Column(db.Integer, db.ForeignKey("shipment.id"))
    shipments = db.relationship("Shipment", backref="inventory", lazy=True)
    

    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "quantity": self.quantity,
            "price" : self.price

        }
        
    @classmethod
    def get_all_inventories(cls):
        return cls.query.all()