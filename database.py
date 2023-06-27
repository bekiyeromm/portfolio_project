from sqlalchemy import create_engine, text
from flask import jsonify,request,redirect,render_template
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

def load_emp_from_db():
    with engine.connect() as conn:
        res = conn.execute(text("select * from emp"))
        res_dict = []
        for row in res.all():
            name, email,link = row  # Extract the values from the row
            res_dict.append({"name": name, "email": email, "link": link})  # Create a dictionary
        return res_dict
# insert data into emp database
def insert_into_emp_db(dataa):
    with engine.connect() as conn:
        res = text("INSERT INTO emp (name, email, link) VALUES (:name, :email, :link)")
        conn.execute(res, {"name": dataa['name'], "email": dataa['email'], "link": dataa['link']})
        conn.commit()
        redirect ('home.html')

# search all data from emp database using 
def search_data_from_emp():
    with engine.connect() as conn:
        result = conn.execute(text("select * from emp")).fetchall()
        # employees = []
        # for emp in result.all():
        #     id,fn,email,link = emp
        #     employees.append({"id":id,"name":fn,"email":email,"link":link})
        return result

# insert into drug database
def show_drug():
    with engine.connect() as conn:
        result = conn.execute(text("select * from medicine"))
        result_dict = []
        for row in result.all():
            id,name,manufacturer,price,quantity = row  # Extract the values from the row
            result_dict.append({"id": id, "name": name, "manufacturer": manufacturer,"price": price, "quantity": quantity})  # Create a dictionary
        return result_dict
    
# insert into medicine table   
def insert_into_drug_db(drug_data):
    with engine.connect() as con:
        med = text("INSERT INTO medicine (name, manufacturer, price, quantity) VALUES ( :name, :manufacturer, :price, :quantity)")
        con.execute(med, {"name": drug_data['name'], "manufacturer": drug_data['manufacturer'], "price": drug_data['price'], "quantity": drug_data['quantity']})
        con.commit()
