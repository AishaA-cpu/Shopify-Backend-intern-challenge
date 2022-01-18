from http import HTTPStatus


class Inventory_helpers:
    def record_not_found(Inventory, Inventory_id):
        return {
            "message" : f"{Inventory} {Inventory_id} not found"
        }, HTTPStatus.NOT_FOUND

