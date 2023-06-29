from flask import Flask,render_template, jsonify,request,redirect
from sqlalchemy import text
from drug import engine, show_drug, insert_into_drug_db,delete_drug_db
from employee import search_data_from_emp, load_employe_from_db,delete_emp_db
from employee import insert_into_emp_db, load_users_from_db
app = Flask(__name__)
	


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


@app.route('/delete_employee', methods=['POST'])
def delete_employee():
	employee_id = request.form["employee_id"]
	delete_emp_db(employee_id)
	return render_template('delete_emp_submited.html', dell=employee_id)

@app.route("/update_employe_form")
def update_employee_form():
    return render_template("update_employee.html")

@app.route('/update_employe', methods=['post'])
def update_employee():
	employee_id = request.form["employee_id"]
	name = request.form["name"]
	contact = request.form["contact"]
	sex = request.form["sex"]
	address = request.form["address"]
	with engine.connect() as conn:
		res = text("UPDATE Employee SET Name=:name, Contact=:contact, Sex=:sex, Address=:address WHERE EmployeeID=:employee_id")
		conn.execute(res, {"name": name, "contact": contact, "sex": sex, "address": address, "employee_id": employee_id})
		conn.commit()
		return redirect("/home.html")

@app.route('/delete_drug', methods=['POST'])
def delete_drugg():
	drug_id = request.form["drug_id"]
	delete_drug_db(drug_id)
	return render_template('delete_drug_submited.html', drugg=drug_id)


if __name__ == ('__main__'):
	app.run(host='0.0.0.0', debug = True);
