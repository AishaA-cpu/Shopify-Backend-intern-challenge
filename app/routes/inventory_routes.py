from flask import Blueprint, jsonify, request
import requests
from app import db
from http import HTTPStatus
from app.models.inventory import Inventory
from app.models.route_helper_methods import Inventory_helpers

I = Inventory_helpers()

inventory_bp = Blueprint("inventory_bp", __name__, url_prefix= "/inventories")


@inventory_bp.route("", methods=["GET"])
def get_all_inventory_items():
    """
    Gets a list of all inventory items in data base 
    returns an empty list if no items are avaialble in database
    uses class method to get all inventories
    uses instance method to generate response for each inventory
    jsonify converts a list to a json object
    """
    # new_list = [item for item in data]
    inventories = [inventory.to_json() for inventory in Inventory.get_all_inventories()]

    return jsonify(inventories), 200

@inventory_bp.route("/<inventory_id>", methods=["GET"])
def get_one_inventory_item(inventory_id):
    """
    Gets one inventory item from database by unique inventory id 
    returns error if not found 
    """
    inventory = Inventory.query.get(inventory_id)

    if inventory is None:
        return I.inventory_not_found(inventory_id), HTTPStatus.NOT_FOUND

    return inventory.to_json(), HTTPStatus.OK

@inventory_bp.route("/<inventory_id>", methods=["DELETE"])
def delete_one_inventory_item(inventory_id):
    """
    Deletes one inventory item by inventory id
    returns 200 on success, 404 if inventory to delete is not 
    available. 
    """
    inventory = Inventory.query.get(inventory_id)

    if inventory is None:
        return I.inventory_not_found(inventory_id), HTTPStatus.NOT_FOUND

    db.session.delete(inventory)
    db.session.commit()

    return {
        "id" : inventory.id,
        "message": f"Inventory {inventory_id} successfully deleted"
    }, HTTPStatus.OK

@inventory_bp.route("", methods=["POST"])
def create_inventory_item():
    """
    Creates one inventory item checks that all attributes
    to create inventory are in the post request
    if post request is missing any of the fields, 
    specify bad request
    """
    request_body =  request.get_json()

    missing_requirements = I.bad_request(request_body)

    if missing_requirements:
        missing_requirements = list(missing_requirements)
        missing_requirements.sort()
        return {
            "message" : f"please include {missing_requirements} to create inventory"
        }, HTTPStatus.BAD_REQUEST

    new_inventory = Inventory(
        name=request_body["name"],
        quantity=request_body["quantity"],
        price = request_body["price"]
    )

    db.session.add(new_inventory)
    db.session.commit()

    return {
        "inventory" : new_inventory.to_json()
        }, HTTPStatus.CREATED
    

@inventory_bp.route("/<inventory_id>", methods=["PUT"])
def put_inventory_item(inventory_id):
    """
    This route modifies an exsisting inventory item,
    and replaces the item in data
    requires name and quantity in the put request
    uses helper returns not found if inventory is not available
    returns bad request if the request is missing any fields 
    """
    request_body =  request.get_json()
    inventory = Inventory.query.get(inventory_id)

    if inventory is None:
        return I.inventory_not_found(inventory, inventory_id), HTTPStatus.NOT_FOUND
    
    missing_requirements = I.bad_request(request_body)
    if missing_requirements:
        return {
            "message" : f"please include {missing_requirements} to update inventory"
        }, HTTPStatus.BAD_REQUEST

    inventory.name = request_body["name"]
    inventory.quantity = request_body["quantity"]
    inventory.price = request_body["price"]

    db.session.commit()

    return {
        "inventory" : inventory.to_json()
    }, HTTPStatus.OK

    
