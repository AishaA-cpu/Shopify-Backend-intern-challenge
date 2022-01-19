from app.models.inventory import Inventory
from app.models.shipments import Shipment
import pytest

# The assert act and assert portions of the test
# these tests make calls to the routes using the data created in conftest.py

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
    assert response_body == {
            
                "id" : 2,
                "name": "Tops",
                "quantity" : 2
            }

def test_get_one_inventory_by_id_not_found(client, two_inventory):
    response = client.get("/inventories/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
                "message" : f"inventory 3 not found"
            }

def test_post_all_no_name(client):
    response = client.post("/inventories", json={
        "quantity": 1
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "message" : "make sure name and quatity are specified"
    }

def test_create_one_inventory(client):
    response = client.post("/inventories", json={
        "quantity":1,
        "name": "shoes"
    })
    response_body =response.get_json()

    assert response.status_code == 201
    assert response_body == { 
        "inventory" :
                    {"id" : 1,
                    "name" : "shoes",
                    "quantity": 1}
    }

def test_delete_one_inventory(client, one_inventory):
    response = client.delete("/inventories/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "message": f"Inventory 1 successfully deleted"
    }

    assert Inventory.query.get(1) == None


def test_update_inventory(client, one_inventory):
    response = client.put("/inventories/1", json={
        "name":"blouse",
        "quantity": 5
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "inventory":{
            "id" : 1,
            "name": "blouse",
            "quantity": 5
        }
    }

    inventory = Inventory.query.get(1)
    assert inventory.name == "blouse"
    assert inventory.quantity == 5



def test_create_one_shipment(client):
    response = client.post("/shipments", json={
        "address" : "Shopify Offices"
    })

    response_body = response.get_json()
    assert response.status_code == 201

    assert response_body == {
        "shipment" : f"new shipment created for Shopify Offices"
    }
    new_shipment = Shipment.query.get(1)
    assert new_shipment
    assert new_shipment.address == "Shopify Offices"


def test_assign_inventory_to_shipment(client, one_shipment, two_inventory):
    response = client.post("/shipments/1/assign_inventory", json={
        "inventory_id": [1, 2]
    })
    reponse_body = response.get_json()
    assert response.status_code == 200
    assert reponse_body == {
        "id": 1,
        "inventories" : [1, 2]
    }

    inventory1 = Inventory.query.get(1)
    inventory2 = Inventory.query.get(2)

    assert inventory1.quantity == 0
    assert inventory2.quantity == 1