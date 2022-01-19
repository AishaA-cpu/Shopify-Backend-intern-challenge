from app import db

# the inventory model, 1 class method to get 
# all stores inventories in the class
# to_json instance method returns the attrubutes 
# of the object
# inventory inherits from the SQLA base model
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    shipment_id = db.Column(db.Integer, db.ForeignKey("shipment.id"))
    shipments = db.relationship("Shipment", backref="inventory", lazy=True)
    

    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "quantity": self.quantity

        }
        
    @classmethod
    def get_all_inventories(cls):
        return cls.query.all()
