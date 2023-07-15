from sqlalchemy import create_engine, text
from flask import jsonify, request, redirect, render_template
from models.employee import engine
import models.inventory as inventory


def insert_sales_into_database(inventory_id, quantity, price, sales_date):
    with engine.connect() as conn:
        """Check if the quantity of the drug is sufficient and
        if so, insert the sold drug into sales table"""
        check_query = "SELECT Quantity FROM Inventory WHERE InventoryID = :inventory_id"
        check_values = {"inventory_id": inventory_id}
        result = conn.execute(text(check_query), check_values).fetchone()
        if result is None:
            return "Invalid Medication ID"

        current_quantity = result[0]
        if current_quantity < quantity:
            return "Insufficient quantity of drug"
        """updates sales table"""
        insert_query = "INSERT INTO Sales (InventoryID, QuantitySold, Price, SaleDate) VALUES (:inventory_id, :quantity, :price, :sales_date)"
        insert_values = {"inventory_id": inventory_id, "quantity": quantity, "price": price, "sales_date": sales_date}
        conn.execute(text(insert_query), insert_values)
        """Update inventory data"""
        update_query = "UPDATE Inventory SET Quantity = Quantity - :quantity_sold WHERE InventoryID = :inventory_id"
        update_values = {"quantity_sold": quantity, "inventory_id": inventory_id}
        conn.execute(text(update_query), update_values)
        conn.commit()
    return ("drug sold successfully")

    """receipt_url = "/generate_receipt/{}".format(result.lastrowid)  # Assuming last inserted sale ID
    return "Drug sold successfully! Receipt: <a href='{}' target='_blank'>View Receipt</a>".format(receipt_url)
    """


def view_sold_drug():
    """retrives all the sold Drug from the sale table"""
    with engine.connect() as conn:
        res = conn.execute(text("select * from Sales")).fetchall()
        return (res)


def delete_from_sales_db(sale_id):
    """delete specific sold drug using sale id"""
    with engine.connect() as conn:
        delete_query = "DELETE FROM Sales WHERE SaleID = :sale_id"
        conn.execute(text(delete_query), {"sale_id": sale_id})
        conn.commit()
