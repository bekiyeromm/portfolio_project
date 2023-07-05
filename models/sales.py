from sqlalchemy import create_engine, text
from flask import jsonify,request,redirect,render_template
from models.employee import engine
import models.inventory as inventory



# def insert_sales_into_database(medication_id, quantity, price, sales_date):
#     with engine.connect() as conn:
#         query = "INSERT INTO Sales (MedicationID, QuantitySold, Price, SaleDate) VALUES (:medication_id, :quantity, :price, :sales_date)"
#         values = {"medication_id": medication_id, "quantity": quantity, "price": price, "sales_date": sales_date}
#         conn.execute(text(query), values)
#         conn.commit()
#         #update
#         # inventory.Quantity
#         update_query = "UPDATE Inventory SET Quantity = Quantity - :quantity_sold WHERE MedicationID = :medication_id"
#         update_values = {"quantity_sold": quantity, "medication_id": medication_id}
#         conn.execute(text(update_query), update_values)
#         conn.commit()
#     return "Drug sold successfully!"

def insert_sales_into_database(inventory_id, quantity, price, sales_date):
    with engine.connect() as conn:
        # Check if the quantity of the drug is sufficient
        check_query = "SELECT Quantity FROM Inventory WHERE InventoryID = :inventory_id"
        check_values = {"inventory_id": inventory_id}
        result = conn.execute(text(check_query), check_values).fetchone()
        
        if result is None:
            return "Invalid Medication ID"
        
        current_quantity = result[0]
        
        if current_quantity < quantity:
            return "Insufficient quantity of drug"
        
        # Update sales data
        insert_query = "INSERT INTO Sales (InventoryID, QuantitySold, Price, SaleDate) VALUES (:inventory_id, :quantity, :price, :sales_date)"
        insert_values = {"inventory_id": inventory_id, "quantity": quantity, "price": price, "sales_date": sales_date}
        conn.execute(text(insert_query), insert_values)
        
        # Update inventory data
        update_query = "UPDATE Inventory SET Quantity = Quantity - :quantity_sold WHERE InventoryID = :inventory_id"
        update_values = {"quantity_sold": quantity, "inventory_id": inventory_id}
        conn.execute(text(update_query), update_values)
        
        conn.commit()
    
    return "Drug sold successfully!"


def view_sold_drug():
    with engine.connect() as conn:
        res = conn.execute(text("select * from Sales")).fetchall()
        return (res)
    
    
def delete_from_sales_db(sale_id):
    with engine.connect() as conn:
        delete_query = "DELETE FROM Sales WHERE SaleID = :sale_id"
        conn.execute(text(delete_query), {"sale_id": sale_id})
        conn.commit()


# def update_sales(data):
#     with engine.connect() as conn:
#         res = text("UPDATE Sales SET MedicationID = :medication_id, QuantitySold = :quantity_sold, Price = :price, SaleDate = :sale_date WHERE SaleID = :sale_id")
#         conn.execute(res, {"medication_id": data['medication_id'], "quantity_sold": data['quantity_sold'], "price": data['price'], "sale_date": data['sale_date'], "sale_id": data['sale_id']})
#         conn.commit()
#         update_query = "UPDATE Inventory SET Quantity = Quantity - :quantity_sold WHERE MedicationID = :medication_id"
#         update_values = {"quantity_sold": data['quantity_sold'], "medication_id": data['medication_id']}
#         conn.execute(text(update_query), update_values)
#         conn.commit()