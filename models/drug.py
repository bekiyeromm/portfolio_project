from sqlalchemy import create_engine, text
from flask import jsonify, request, redirect, render_template
from models.employee import engine


def insert_into_drug_db(drugg):
    """insert_into_drug_db"""
    with engine.connect() as con:
        drg = text(
            "INSERT INTO Drug (DrugID, Name, Manufacturer, ExpiryDate) VALUES (:id, :name, :manufacturer, :expirydate)")
        con.execute(drg, {"id": drugg['id'], "name": drugg['name'],
                    "manufacturer": drugg['manufacturer'], "expirydate": drugg['expirydate']})
        con.commit()


def show_drug():
    """ ishow all the available data of Drug table in the database"""
    with engine.connect() as conn:
        result = conn.execute(text("select * from Drug")).fetchall()
        return result


def delete_drug_db(drug_id):
    """deletes drug item from  drug table"""
    with engine.connect() as conn:
        res = text("DELETE FROM Drug WHERE DrugID = :drug_id")
        conn.execute(res, {"drug_id": drug_id})
        conn.commit()


def update_drug_in_drug_db(data):
    """updates  drug item in  drug table using Drug id"""
    with engine.connect() as conn:
        res = text(
            "UPDATE Drug SET Name = :name, Manufacturer = :manufacturer, ExpiryDate = :expiry_date WHERE DrugID = :drug_id")
        conn.execute(res, {"name": data['name'], "manufacturer": data['manufacturer'],
                     "expiry_date": data['expiry_date'], "drug_id": data['drug_id']})
        conn.commit()
