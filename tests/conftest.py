import pytest
from app import create_app
from app.models.inventory import Inventory
from app.models.shipments import Shipment
from app import db
from flask.signals import request_finished

# The testing method follows Arrange, Act, Assert steps
# this is the arrange step of the tests
# # simulates record to be posted in the database 

INVENTORY_NAME = "Pants"
INVENTORY_QUANTITY = 1

INVENTORY2_NAME = "Tops"
INVENTORY2_QUANTITY = 2

SHIPMENT_ADRESS = "Shopify Offices"

# ARRANGE, ACT, ASSERT
# this file handles the arrange portion of the unit tests 

@pytest.fixture
def app():
    app = create_app({"TESTING": True})


    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_inventory(app):
    new_inventory = Inventory(
        name = INVENTORY_NAME,
        quantity = INVENTORY_QUANTITY
    )

    db.session.add(new_inventory)
    db.session.commit()

@pytest.fixture
def two_inventory(app):
    db.session.add_all([
    Inventory(
        name = INVENTORY_NAME,
        quantity = INVENTORY_QUANTITY
    ),

    Inventory(
        name = INVENTORY2_NAME,
        quantity = INVENTORY2_QUANTITY
    )]
    )
    db.session.commit()

@pytest.fixture
def one_shipment(app):
    new_shipment = Shipment(
        address = SHIPMENT_ADRESS
        )
    db.session.add(new_shipment)
    db.session.commit()
