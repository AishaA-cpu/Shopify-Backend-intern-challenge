from operator import length_hint
from flask import Blueprint, jsonify, make_response, request
import requests
from app import db
from http import HTTPStatus
from datetime import datetime
from app.models.shipments import Shipment
from app.models.inventory import Inventory
from app.models.route_helper_methods import Shipment_helpers

S = Shipment_helpers()


shipment_bp = Blueprint("shipment_bp", __name__, url_prefix= "/shipments")

@shipment_bp.route("", methods=["POST"])
def create_one_shipment():
    """
    creates one shipment, returns 201 status code for created and commited to db
    400 for bad request if post request has missing attributes 

    """
    request_body = request.get_json()
    
    missing_requirements = S.bad_shipment_request(request_body)

    if missing_requirements:
        return {
            "message" : f"please include {missing_requirements} to create shipment"
        }, HTTPStatus.BAD_REQUEST

    new_shipment = Shipment(
        address =  request_body["address"],
        name = request_body["name"],
        length = request_body["length"],
        breadth = request_body["breadth"],
        width = request_body["width"],
        weight = request_body["weight"],
        created_date = datetime.now()
    )

    db.session.add(new_shipment)
    db.session.commit()

    return {
        "shipment" : new_shipment.to_json()
        }, HTTPStatus.CREATED




@shipment_bp.route("/<shipment_id>/assign_inventory", methods=["POST"])
def attach_inventory_to_shipment(shipment_id):
    """
    route takes a list of inventories and attaches one of each inventory item to a shipment 
    updates inventory quantity, deducts one from each inventory 
    item if it has been assigned to a shipment
    . returns 404 if shipment is not available 
    returns 200 for successful assignment, a dictionay with shipment id and a list of inventories
    uses list comprehension. SQLA returns an list object for relationship objects
    """
    request_body = request.get_json()

    shipment = Shipment.query.get(shipment_id)

    if not shipment:
        return S.Shipment_not_found(shipment_id), HTTPStatus.NOT_FOUND

    for inventory_id in request_body["inventory_id"]:
        inventory = Inventory.query.get(inventory_id)
        if inventory.quantity <= 0:
            return {
                "message" : f"{inventory.name} with {inventory.id} is not available"
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        shipment.inventory.append(inventory)
        inventory.quantity -= 1
    
    db.session.commit()
    
    
    return {
        "id" : shipment.id,
        "inventories": [inventory.id for inventory in shipment.inventory]
    }, HTTPStatus.OK


