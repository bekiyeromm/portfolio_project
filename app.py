from flask import Flask,render_template, jsonify,request,redirect
from sqlalchemy import text
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
from models.drug import engine, show_drug, insert_into_drug_db,delete_drug_db,update_drug_in_drug_db
from models.employee import search_data_from_emp, update_employee_in_emp_db,delete_emp_db
from models.employee import insert_into_emp_db, load_users_from_db
from models.inventory import insert_into_inventory,show_inv_data,delete_inventory, update_inventory
from models.sales import insert_sales_into_database,view_sold_drug,delete_from_sales_db


app = Flask(__name__)
load_dotenv()	

connection_string = os.getenv('DATABASE_CONNECTION_STRING')
engine = create_engine(connection_string)

@app.route('/')
def home():
	user = load_users_from_db()
	return render_template('login.html', jobs = user);

 # creating api to retrive the user email and pass as json file
@app.route("/main")
def main():
	return render_template('home.html')

# api to render login.html
@app.route('/login', methods=['POST'])
def login():
	
	username = request.form['username']
	password = request.form['password']
	try:
		with engine.connect() as conn:
			query = text("SELECT * FROM user WHERE username = :username AND password = :password")
			result = conn.execute(query, {"username": username, "password": password})
			userr = result.fetchone()
			if userr:
            # Redirect to the home page or display a success message
				return redirect('/main')
			else:
            # Display an error message for invalid credentials
				return render_template('login.html', error_message='Invalid username or password')
	except Exception as e:
		# Display an error message for any exception
		return render_template('login.html', error_message=str(e))
	return render_template('login.html')
		
    



@app.route("/signup")
def reg_employe():
	# emp = load_employe_from_db()
	return render_template('regform.html')


@app.route("/about")
def about():
	return render_template('aboutus.html')


# @app.route("/regg", methods = ['post'])
# def regster():
# 	dataa = load_emp_from_db()
# 	return render_template("app_submited.html",app=dataa)
# 	# return jsonify(dataa)

# # display data from the form as json file
# @app.route("/regg", methods = ['post'])
# def register():
# 	data_from_form = request.form
# 	#return jsonify(dataa)
# 	return render_template('app_submited.html', form_data=data_from_form)

# insert form data into emp table
@app.route("/regg", methods = ['post'])
def register_emp():
	data_from_form = request.form
	insert_into_emp_db(data_from_form)
	return render_template("app_submited.html", form_data=data_from_form)

@app.route("/search")
def display_all_employe():
	emp_s = search_data_from_emp()
	return render_template("show_employee.html", emp_s=emp_s)

@app.route('/delete_employee', methods=['POST'])
def delete_employee():
	employee_id = request.form["employee_id"]
	delete_emp_db(employee_id)
	return redirect('/search')

@app.route("/update_employe_form")
def update_employee_form():
    return render_template("update_employee.html")

@app.route('/update_employee', methods=['POST'])
def update_employee():
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

#################   Drug     ##############

@app.route('/regg_drug_form')
def drugg_reg():
	return render_template('drug_reg.html')

@app.route('/push_drug', methods=['post'])
def insert_drug():
	dataa = request.form
	print("hello")
	insert_into_drug_db(dataa)
	return render_template('drug_submited.html', da=dataa)

# display list of available drug
@app.route('/show_drug')
def display_drug():
	drug_data = show_drug()
	return render_template('drug_show.html', drug_data=drug_data)


@app.route('/delete_drug', methods=['POST'])
def delete_drugg():
	drug_id = request.form["drug_id"]
	delete_drug_db(drug_id)
	return render_template('delete_drug_submited.html', drugg=drug_id)

@app.route('/sell_drug_form')
def sel_drug():
	return render_template('sell_form_reg.html')

@app.route('/update_drug_form')
def update_drug_form():
	return render_template('update_drug.html')

@app.route('/update_drug', methods=['post'])
def update_drug():
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
	return render_template('inventory.html')

@app.route('/show_inventory')
def display_inventory_data():
	inv=show_inv_data()
	return render_template('inventory_show.html', inv=inv)


@app.route('/delete_inventory', methods=['POST'])
def del_inventory():
	inv_id = request.form['inventory_id']
	delete_inventory(inv_id)
	return redirect('/show_inventory')

@app.route('/show_inventory', methods=['post'])
def insert_into_inv():
	data=request.form
	insert_into_inventory(data)
	return ("inventory item added successfully")

@app.route('/update_inv_form')
def update_inv_form():
	return render_template('update_inventory.html')

@app.route('/update_inventory', methods=['POST'])
def update_inv():
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
	if request.method == 'POST':
		inventory_id = request.form['inventory_id']
		quantity = int(request.form['quantity'])
		price = float(request.form['price'])
		sales_date = request.form['sales_date']
		insert_sales_into_database(inventory_id, quantity, price, sales_date)
		# return "Sales data inserted successfully!"
	return redirect('/sold_drug')

@app.route('/sold_drug')
def show_sold_drug():
	sold_drug=view_sold_drug()
	return render_template('sell_form.html',sold_drug=sold_drug)

@app.route('/delete_sales', methods=['POST'])
def del_sales():
	sale_id = request.form['sale_id']
	delete_from_sales_db(sale_id)
	return redirect('/sold_drug')


@app.route('/update_sales_form')
def update_sales_form():
	return render_template('update_sales.html')


# @app.route('/update_sales', methods=['POST'])
# def update_sales_route():
#     if request.method == 'POST':
#         sale_id = request.form['sale_id']
#         medication_id = request.form['medication_id']
#         quantity_sold = request.form['quantity_sold']
#         price = request.form['price']
#         sale_date = request.form['sale_date']
#         data = {
#             'sale_id': sale_id,
#             'medication_id': medication_id,
#             'quantity_sold': quantity_sold,
#             'price': price,
#             'sale_date': sale_date
#         }
#         update_sales(data)
#     return redirect('/sold_drug')



if __name__ == ('__main__'):
	app.run(host='0.0.0.0', debug = True)