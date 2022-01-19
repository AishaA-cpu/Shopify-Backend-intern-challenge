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
    request_body = request.get_json()

    if S.bad_shipment_request(request_body):
        return {
            "message" : "Include a shipment address"
        }, HTTPStatus.BAD_REQUEST

    new_shipment = Shipment(
        address =  request_body["address"],
        created_date = datetime.now()
    )

    db.session.add(new_shipment)
    db.session.commit()

    return {
        "shipment" : f"new shipment created for {new_shipment.address}"
    }, HTTPStatus.CREATED




@shipment_bp.route("/<shipment_id>/assign_inventory", methods=["POST"])
def attach_inventory_to_shipment(shipment_id):
    request_body = request.get_json()

    shipment = Shipment.query.get(shipment_id)

    if not shipment:
        return S.Shipment_not_found(shipment_id), HTTPStatus.NOT_FOUND

    for inventory_id in request_body["inventory_id"]:
        inventory = Inventory.query.get(inventory_id)
        shipment.inventory.append(inventory)
        inventory.quantity -= 1
    
    db.session.commit()

    return {
        "id" : shipment.id,
        "inventories": [inventory.id for inventory in shipment.inventory]
    }


