import pytest
from app import create_app
from app.models.inventory import Inventory
from app.models.shipments import Shipment
from app import db
from flask.signals import request_finished

