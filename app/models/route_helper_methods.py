

class Inventory_helpers:
    def inventory_not_found(Inventory, Inventory_id):
        return {
            "message" : f"{Inventory} {Inventory_id} not found"
        }

    def bad_request(json):
        return "name" not in json or "quantity" not in json

class Shipment_helpers:
    def Shipment_not_found(Shipment, Shipment_id):
        return {
            "message" : f"{Shipment} {Shipment_id} not found"
        }

    def bad_shipment_request(json):
        return "address" not in json