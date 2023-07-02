from sqlalchemy import create_engine, text
from flask import jsonify,request,redirect,render_template
from employee import engine


# insert into medicine table    insert_into_drug_db
def insert_into_drug_db(drugg):
    with engine.connect() as con:
        drg = text("INSERT INTO Drug (DrugID, Name, Manufacturer, ExpiryDate) VALUES (:id, :name, :manufacturer, :expirydate)")
        con.execute(drg, {"id": drugg['id'], "name": drugg['name'], "manufacturer": drugg['manufacturer'], "expirydate": drugg['expirydate']})
        con.commit()

# insert into drug database
def show_drug():
    with engine.connect() as conn:
        result = conn.execute(text("select * from Drug")).fetchall()
        # result_dict = []
        # for row in result:
        #     id,name,manufacturer,expirydate= row  # Extract the values from the row
        #     result_dict.append({"DrugId": id, "Name": name, "Manufacturer": manufacturer,"ExpiryDate": expirydate})  # Create a dictionary
        return result
    
def delete_drug_db(drug_id):
    with engine.connect() as conn:
        res = text("DELETE FROM Drug WHERE DrugID = :drug_id")
        conn.execute(res, {"drug_id": drug_id})
        conn.commit()

def update_drug_in_drug_db(data):
    with engine.connect() as conn:
        res = text("UPDATE Drug SET Name = :name, Manufacturer = :manufacturer, ExpiryDate = :expiry_date WHERE DrugID = :drug_id")
        conn.execute(res, {"name": data['name'], "manufacturer": data['manufacturer'], "expiry_date": data['expiry_date'], "drug_id": data['drug_id']})
        conn.commit()