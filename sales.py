from sqlalchemy import create_engine, text
from flask import jsonify,request,redirect,render_template
from employee import engine
import inventory



def insert_sales_into_database(medication_id, quantity, price, sales_date):
    with engine.connect() as conn:
        query = "INSERT INTO Sales (MedicationID, QuantitySold, Price, SaleDate) VALUES (:medication_id, :quantity, :price, :sales_date)"
        values = {"medication_id": medication_id, "quantity": quantity, "price": price, "sales_date": sales_date}
        conn.execute(text(query), values)
        conn.commit()
        #update
        # inventory.Quantity
        update_query = "UPDATE Inventory SET Quantity = Quantity - :quantity_sold WHERE MedicationID = :medication_id"
        update_values = {"quantity_sold": quantity, "medication_id": medication_id}
        conn.execute(text(update_query), update_values)
        conn.commit()
    return "Drug sold successfully!"


def view_sold_drug():
    with engine.connect() as conn:
        res = conn.execute(text("select * from Sales")).fetchall()
        return (res)