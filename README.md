# Shopify-Backend-intern-challenge

project demonstrates basic CRUD operations and an enhancement (Ability to create “shipments” and assign inventory to the shipment,
and adjust inventory appropriately)

It uses a dev and test database for unit testing, appropriate database is selected in the app/_init__ file
but the user needs just a test database


Uses the python language and pip package handler, please have them installed

Flask framework

Uses SQLALCHEMY, an ORM and alembic a tool to support SQLALCHEMY database migrations they work with the flask framework.

Setup Steps


Clone repo, cd into repo and create a virtual env in your dir
create virtual env, -python -m venv venv
activate vitual env, - source venv/bin/activate
verify that you are working in a python virtual env
    python --version should output a Python 3 version
    pip --version

required dependencies for this project are in the requirements.txt,
it is recommended to install dependencies in a virtual ENV
pip install -r requirements.txt


create a .ENV file and set environment variables to point to data base
please use the "SQLALCHEMY_TEST_DATABASE_URI" or

conftest file creates and drops(cleans up) records in your test database for testing purposes

e.g "SQLALCHEMY_TEST_DATABASE_URI"= "postgresql+psycopg2: path/to/your/test/database"

After creating database and connection string:

one time setup, -> run flask db init to init database
app/tests/test_route.py -> holds all integration tests for the routes


EXAMPLE SEQUENCE DIAGRAM OF ONE OF THE ROUTES


ERD OF CLASSES








TASK: Build an inventory tracking web application for a logistics company. We are looking for a web application that meets the requirements listed below, along with one additional feature, with the options also listed below.

Requirements:

Basic CRUD Functionality. You should be able to:
Create inventory items
Edit Them
Delete Them
View a list of them

ONE OF THE FOLLOWING (We will only evaluate the first feature chosen, so please only choose one)

Push a button export product data to a CSV
Allow image uploads AND store image with generated thumbnails
When deleting, allow deletion comments and undeletion
Filtering based on fields/inventory count/tags/other metadata
Ability to assign/remove inventory items to a named group/collection
Ability to create warehouses/locations and assign inventory to specific locations
Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately
Ability to generate a report on inventory levels over time, like: most in-stock or out-of-stock last month
