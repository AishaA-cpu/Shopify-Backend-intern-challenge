

class Inventory_helpers:
    def inventory_not_found(self, Inventory_id):
        return {
            "message" : f"inventory {Inventory_id} not found"
        }

    def bad_request(self, json):
        return "name" not in json or "quantity" not in json



class Shipment_helpers:
    def Shipment_not_found(self, Shipment_id):
        return {
            "message" : f"shipment {Shipment_id} not found"
        }

    def bad_shipment_request(self, json):
        return "address" not in json