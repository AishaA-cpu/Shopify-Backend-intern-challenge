import pytest
from app import create_app
from app.models.inventory import Inventory
from app.models.shipments import Shipment
from app import db
from flask.signals import request_finished

# Creates data for database for pytest unit tests

INVENTORY_NAME = "Pants"
INVENTORY_QUANTITY = 1

# ARRANGE, ACT, ASSERT
# this file handles the arrange portion of the unit tests 

@pytest.fixture
def app():
    app = create_app({"TESTING": True})



    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

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

