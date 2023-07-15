from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy import text
from dotenv import load_dotenv
from sqlalchemy import create_engine
import datetime
import os
from models.drug import engine, show_drug, insert_into_drug_db
from models.drug import delete_drug_db, update_drug_in_drug_db
from models.employee import delete_emp_db
from models.employee import insert_into_emp_db, load_users_from_db
from models.employee import search_data_from_emp, update_employee_in_emp_db
from models.inventory import insert_into_inventory, show_inv_data
from models.inventory import delete_inventory, update_inventory
from models.sales import insert_sales_into_database, view_sold_drug
from models.sales import delete_from_sales_db


app = Flask(__name__)
load_dotenv()

connection_string = os.getenv('DATABASE_CONNECTION_STRING')
engine = create_engine(connection_string)


@app.route('/')
def landing():
    """an api to render the landing page"""
    return render_template('landing.html')


@app.route('/login')
def home():
    """an api route to render user login page"""
    user = load_users_from_db()
    return render_template('login.html', user=user)


@app.route("/main")
def main():
    """an api route to render home page"""
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
    """api route retrive json data from html form and from,
    database table checks if both value matches, if so
    allows the user to navigate into home page"""
    username = request.form['username']
    password = request.form['password']
    try:
        with engine.connect() as conn:
            query = text(
                "SELECT * FROM user WHERE username = :username AND password = :password")
            result = conn.execute(
                query, {"username": username, "password": password})
            userr = result.fetchone()
            if userr:
                """Redirect to the home page or display a success message"""
                return redirect('/main')
            else:
                """Display an error message for invalid credentials"""
                return render_template('login.html', error_message='Invalid username or password')
    except Exception as e:
        """Display an error message for any exception"""
        return render_template('login.html', error_message=str(e))


@app.route("/signup")
def reg_employe():
    """renders the user into Employee registration form"""
    return render_template('regform.html')


@app.route("/about")
def about():
    """renders about page"""
    return render_template('aboutus.html')


@app.route("/regg", methods=['post'])
def register_emp():
    """insert form data into emp table"""
    data_from_form = request.form
    insert_into_emp_db(data_from_form)
    return render_template("app_submited.html", form_data=data_from_form)


@app.route("/search")
def display_all_employe():
    """displayes all the employes in to the show_employee page"""
    emp_s = search_data_from_emp()
    return render_template("show_employee.html", emp_s=emp_s)


@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    """deletes an employe using Employe id and redirects the
    user into the show Employe page"""
    employee_id = request.form["employee_id"]
    delete_emp_db(employee_id)
    return redirect('/search')


@app.route("/update_employe_form")
def update_employee_form():
    """renders the user into the user update form"""
    return render_template("update_employee.html")


@app.route('/update_employee', methods=['POST'])
def update_employee():
    """updates an employe using Employe id and redirects the
    user into the show Employe page"""
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        contact = request.form['contact']
        sex = request.form['sex']
        address = request.form['address']
        data = {
            'employee_id': employee_id,
            'name': name,
            'contact': contact,
            'sex': sex,
            'address': address
        }
        update_employee_in_emp_db(data)
    return redirect('/search')


@app.route('/regg_drug_form')
def drugg_reg():
    """renders Drug registration form"""
    return render_template('drug_reg.html')


@app.route('/push_drug', methods=['post'])
def insert_drug():
    """inserts a new drug item into drug table and redirect the
    user into the show drug page"""
    dataa = request.form
    insert_into_drug_db(dataa)
    return redirect('/show_drug')


@app.route('/show_drug')
def display_drug():
    """display list of available drug nd redirect the
    user into the show drug page"""
    drug_data = show_drug()
    return render_template('drug_show.html', drug_data=drug_data)


@app.route('/delete_drug', methods=['POST'])
def delete_drugg():
    """delete a specific drug from the drug table using
    drug id and redirects the user into show drug page"""
    drug_id = request.form["drug_id"]
    delete_drug_db(drug_id)
    return redirect('/show_drug')


@app.route('/sell_drug_form')
def sel_drug():
    """renders drug selling form"""
    return render_template('sell_form_reg.html')


@app.route('/update_drug_form')
def update_drug_form():
    """renders update drug form"""
    return render_template('update_drug.html')


@app.route('/update_drug', methods=['post'])
def update_drug():
    """update a specific drug from the drug table using
    drug id and redirects the user into show drug page"""
    if request.method == 'POST':
        drug_id = request.form['id']
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        expiry_date = request.form['expirydate']
        data = {
            'drug_id': drug_id,
            'name': name,
            'manufacturer': manufacturer,
            'expiry_date': expiry_date
        }
        update_drug_in_drug_db(data)
    return redirect('/show_drug')


@app.route('/inventory_reg_form')
def inventory_reg_form():
    """renders invontory rwgistration form"""
    return render_template('inventory.html')


@app.route('/show_inventory')
def display_inventory_data():
    """displays all the available inventory item in the inventory table"""
    inv = show_inv_data()
    return render_template('inventory_show.html', inv=inv)


@app.route('/delete_inventory', methods=['POST'])
def del_inventory():
    """deletes a specific inventory item in the inventory table
    using inventory id"""
    inv_id = request.form['inventory_id']
    delete_inventory(inv_id)
    return redirect('/show_inventory')


@app.route('/show_inventory', methods=['post'])
def insert_into_inv():
    """insert a new inventory item into the inventory table"""
    data = request.form
    insert_into_inventory(data)
    return redirect('/show_inventory')


@app.route('/update_inv_form')
def update_inv_form():
    """renders the update inventory form"""
    return render_template('update_inventory.html')


@app.route('/update_inventory', methods=['POST'])
def update_inv():
    """updates an inventory item using the inventory id and redirects the
    user into show inventory page"""
    if request.method == 'POST':
        inventory_id = request.form['inventoryId']
        medication_id = request.form['medicationId']
        quantity = request.form['quantity']
        location = request.form['location']
        expiry_date = request.form['expiryDate']
        data = {
            'inventory_id': inventory_id,
            'medication_id': medication_id,
            'quantity': quantity,
            'location': location,
            'expiry_date': expiry_date
        }
        update_inventory(data)
    return redirect('/show_inventory')


@app.route('/create_sales', methods=['GET', 'POST'])
def create_sales():
    """creates a sell from the inventory table using inventory id
    and redirec the user into the sold drug table"""
    if request.method == 'POST':
        inventory_id = request.form['inventory_id']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        sales_date = request.form['sales_date']
        insert_sales_into_database(inventory_id, quantity, price, sales_date)
    return redirect('/sold_drug')


@app.route('/sold_drug')
def show_sold_drug():
    """displays all the sold drug item that is found
    in the sales table"""
    sold_drug = view_sold_drug()
    return render_template('sell_form.html', sold_drug=sold_drug)


@app.route('/delete_sales', methods=['POST'])
def del_sales():
    """delete a specific sold drug history from the sales table"""
    sale_id = request.form['sale_id']
    delete_from_sales_db(sale_id)
    return redirect('/sold_drug')


if __name__ == ('__main__'):
    app.run(host='0.0.0.0', debug=True)
