from flask import render_template, redirect, request,jsonify
from sqlalchemy import text
from employee import engine


def show_inv_data():
    with engine.connect() as conn:
        result = conn.execute(text("select * from Inventory")).fetchall()
    return result

def insert_into_inventory(dataa):
    with engine.connect() as conn:
        res = text("INSERT INTO Inventory (InventoryID, MedicationID, Quantity, Location, ExpiryDate) VALUES (:inventory_id, :medication_id, :quantity, :location, :expiry_date)")
        conn.execute(res, {"inventory_id": dataa['inventoryId'], "medication_id": dataa['medicationId'], "quantity": dataa['quantity'], "location":dataa['location'], "expiry_date":dataa['expiryDate']})
        conn.commit()

def delete_inventory(inventory_id):
    with engine.connect() as conn:
        delete_query = "DELETE FROM Inventory WHERE InventoryID = :inventory_id"
        conn.execute(text(delete_query), {"inventory_id": inventory_id})
        conn.commit()