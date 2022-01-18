from app.models.inventory import Inventory
from app.models.shipments import Shipment
import pytest

# The assert step of testing 

def test_get_all_no_saved_inventory(client):
    response = client.get("/inventories")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_inventory_one_saved_inventory(client, one_inventory):
    response = client.get("/inventories")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id" : 1,
            "name": "Pants",
            "quantity" : 1
        }
    ]

def test_get_one_inventory_by_id(client, two_inventory):
    response = client.get("/inventories/2")
    response_body = response.get_json()

    assert response.status_code == 200
    #assert len(response_body) == 1
    assert response_body == {
            
                "id" : 2,
                "name": "Tops",
                "quantity" : 2
            }
    