from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os
from flask import jsonify, request, redirect, render_template

load_dotenv()

connection_string = os.getenv('DATABASE_CONNECTION_STRING')
engine = create_engine(connection_string)


def load_users_from_db():
    """retrives  user from user table """
    with engine.connect() as conn:
        result = conn.execute(text("select * from user"))
        result_dict = []
        for row in result.all():
            username, password = row  # Extract the values from the row
            result_dict.append({"username": username, "password": password})
        return result_dict


def load_employe_from_db():
    """loads all the employees from the employee table"""
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from Employee"))
    employees = []
    for emp in result.all():
        id, name, contact, sex, address = emp
        employees.append({"id": id, "Name": name, "Contact": contact, "Sex": sex, "Address": address})
    return employees


def insert_into_emp_db(dataa):
    """inserts a new Employee into Employee database"""
    with engine.connect() as conn:
        res = text("INSERT INTO Employee (Name, Contact, Sex, Address) VALUES (:name, :contact, :sex, :address)")
        conn.execute(res, {"name": dataa['Name'], "contact": dataa['Contact'], "sex": dataa['Sex'], "address": dataa['Address']})
        conn.commit()
        redirect('home.html')


def search_data_from_emp():
    """search all data from emp database using """
    with engine.connect() as conn:
        result = conn.execute(text("select * from Employee")).fetchall()
        return result


def delete_emp_db(employee_id):
    """deletes an Employee from Employee table using Employee id"""
    with engine.connect() as conn:
        res = text("DELETE FROM Employee WHERE EmployeeID = :employee_id")
        conn.execute(res, {"employee_id": employee_id})
        conn.commit()


def update_employee_in_emp_db(data):
    """updates a specific Employe in Employe table using the
    employee id"""
    with engine.connect() as conn:
        res = text("UPDATE Employee SET Name = :name, Contact = :contact, Sex = :sex, Address = :address WHERE EmployeeID = :employee_id")
        conn.execute(res, {"name": data['name'], "contact": data['contact'], "sex": data['sex'], "address": data['address'], "employee_id": data['employee_id']})
        conn.commit()
