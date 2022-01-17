from app import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    total_quantity = db.Column(db.Integer)

    def to_json(self):
        return {
            "id" : self.inventory.id,
            "name" : self.inventory.name,
            "quantity": self.inventory.quanity

        }
        
    @classmethod
    def get_all_inventories(cls):
        return cls.query.all()