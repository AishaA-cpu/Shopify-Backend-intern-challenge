from flask import Blueprint, jsonify, make_response, request
import requests
from app import db
from http import HTTPStatus
from app.models.inventory import Inventory
from app.models.shipments import Shipment

inventory_bp = Blueprint("inventory_bp", __name__, url_prefix= "/inventories")
shipment_bp = Blueprint("shipment_bp", __name__, url_prefix= "/shipments")

@inventory_bp.route("", methods=["GET"])
def get_all_inventory_items():
    """
    Gets a list of all inventory items in data base 
    returns an empty list if no items are avaialble in database
    """
    

    # request_body = request.get_json()
    # response_body = []
    # inventories = Inventory.query.all()

    # inventories = 

    # for inventory in inventories:
    #     response_body.append(
    #         {
    #             "id" : inventory.id,
    #             "name" : inventory.name,
    #             "quantity" : inventory.quantity
    #         }
    #     )

    # return jsonify(response_body)

    inventories = [Inventory.to_json for inventory in Inventory.get_all_inventories()]

    return jsonify(inventories), 200

@inventory_bp.route("\<inventory_id>", methods=["GET"])
def get_one_inventory_item(inventory_id):
    """
    Gets one inventory item from database by unique inventory id 
    returns error if not found 
    """
    pass

@inventory_bp.route("\<inventory_id>", methods=["DELETE"])
def delete_one_inventory_item(inventory_id):
    """
    Deletes one inventory item
    retruns 200 on success, 400 if bad request
    """
    pass

@inventory_bp.route("", methods=["POST"])
def create_inventory_item():
    """
    Creates one inventory item checks that all attributes are 
    sent in Json
    """
    pass

@inventory_bp.route("\<inventory_id>", methods=["PATCH"])
def create_inventory_item(inventory_id):
    """
    This route modifies an exsisting inventory item,
    does not replace exsiting
    """
    pass