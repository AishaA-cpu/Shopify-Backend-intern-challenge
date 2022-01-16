from flask import Blueprint, jsonify, make_response, request
import requests
from app import db
from http import HTTPStatus
from app.models.inventory import Inventory
from app.models.shipments import Shipment

inventory_bp = Blueprint("inventory_bp", __name__, url_prefix= "/inventories")
shipment_bp = Blueprint("shipment_bp", __name__, url_prefix= "/shipments")

