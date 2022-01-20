# helper methods to catch bad requests 

class Inventory_helpers:
    def inventory_not_found(self, Inventory_id):
        return {
            "message" : f"inventory {Inventory_id} not found"
        }

    def bad_request(self, json):
        required_parameters = {"name", "quantity", "price"}
        set_of_json_keys = set(json.keys())
        return required_parameters - set_of_json_keys

        #return "name" not in json or "quantity" not in json or "price" not in json



class Shipment_helpers:
    def Shipment_not_found(self, Shipment_id):
        return {
            "message" : f"shipment {Shipment_id} not found"
        }

    def bad_shipment_request(self, json):

        required_parameters = {"name", "address", "length", "breadth", "width"}
        set_of_json_keys = set(json.keys())

        return required_parameters - set_of_json_keys

        # return "address" not in json or "name" not in json or "length" \
        # or  "breadth" not in json or "width" not in json