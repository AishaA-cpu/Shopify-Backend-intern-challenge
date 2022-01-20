from app import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime)
    name = db.Column(db.String, nullable=False)
    length = db.Column(db.Float, nullable=False)
    breadth = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id" : self.id,
            "address" : self.address,
            "created_date": self.created_date,
            "name" : self.name,
            "length" : self.length,
            "breadth" : self.breadth,
            "width" : self.width,
            "weight" :  self.weight
        }