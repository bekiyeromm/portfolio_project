from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os
from flask import jsonify,request,redirect,render_template

load_dotenv()

connection_string = os.getenv('DATABASE_CONNECTION_STRING')
engine = create_engine(connection_string)


# login table
def load_users_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from user"))
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
        id,name,contact,sex,address = emp
        employees.append({"id":id,"Name":name,"Contact":contact,"Sex":sex,"Address":address})
    return employees


# insert data into emp database
def insert_into_emp_db(dataa):
    with engine.connect() as conn:
        res = text("INSERT INTO Employee (Name, Contact, Sex, Address) VALUES (:name, :contact, :sex, :address)")
        conn.execute(res, {"name": dataa['Name'], "contact": dataa['Contact'], "sex": dataa['Sex'], "address":dataa['Address']})
        conn.commit()
        redirect ('home.html')

# search all data from emp database using 
def search_data_from_emp():
    with engine.connect() as conn:
        result = conn.execute(text("select * from Employee")).fetchall()
        # employees = []
        # for emp in result.all():
        #     id,fn,email,link = emp
        #     employees.append({"id":id,"name":fn,"email":email,"link":link})
        return result

def delete_emp_db(employee_id):
    with engine.connect() as conn:
        res = text("DELETE FROM Employee WHERE EmployeeID = :employee_id")
        conn.execute(res, {"employee_id": employee_id})
        conn.commit()

def update_employee_in_emp_db(data):
    with engine.connect() as conn:
        res = text("UPDATE Employee SET Name = :name, Contact = :contact, Sex = :sex, Address = :address WHERE EmployeeID = :employee_id")
        conn.execute(res, {"name": data['name'], "contact": data['contact'], "sex": data['sex'], "address": data['address'], "employee_id": data['employee_id']})
        conn.commit()