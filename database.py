from sqlalchemy import create_engine, text
from flask import jsonify
engine = create_engine(
    "mysql+pymysql://pims_user:pims_user_pwd@localhost/pims_db?charset=utf8mb4")

# login table
def load_users_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from login"))
        result_dict = []
        for row in result.all():
            username, password = row  # Extract the values from the row
            result_dict.append({"username": username, "password": password})  # Create a dictionary
        return result_dict

# employe table
def load_employe_from_db():
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from Employee"))
    employees = []
    for emp in result.all():
        id,fn,ln,sex,email,pas = emp
        employees.append({"id":id,"first_name":fn,"last_name":ln,"sex":sex,"email":email,"password":pas})
    return employees
