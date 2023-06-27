from flask import Flask,render_template, jsonify,request,redirect
from sqlalchemy import text
from database import show_drug, insert_into_drug_db,engine
from database import search_data_from_emp, load_employe_from_db
from database import insert_into_emp_db, load_users_from_db, load_emp_from_db
app = Flask(__name__)
	


@app.route('/')
def home():
	user = load_users_from_db()
	return render_template('login.html', jobs = user);

 # creating api to retrive the user email and pass as json file
@app.route("/user")
def list_of_users():
	user = load_users_from_db()
	return jsonify(user)

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
				return redirect('/search')
			else:
            # Display an error message for invalid credentials
				return render_template('login.html', error_message='Invalid username or password')
	except Exception as e:
		# Display an error message for any exception
		return render_template('login.html', error_message=str(e))
	return render_template('login.html')
		
    



@app.route("/signup")
def reg_employe():
	emp = load_employe_from_db()
	return render_template('regform.html', users=emp)


@app.route("/about")
def about():
	return render_template('aboutus.html')

# return json file of employes information
@app.route("/emp/")
def show_employee():
	us = load_employe_from_db()
	# return jsonify(users)
	return render_template('userlist.html', us=us)

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
@app.route("/regg/", methods = ['post'])
def register_emp():
	data_from_form = request.form
	# emp = load_emp_from_db()
	insert_into_emp_db(data_from_form)
	return render_template("app_submited.html", form_data=data_from_form)

@app.route("/search")
def display_all_employe():
	emp_s = search_data_from_emp()
	return render_template("search.html", emp_s=emp_s)
	
@app.route("/medicine/regg", methods=["post", "get"])
def drug_reg():
	drug_data = request.form
	#drug_data = show_drug()
	# return jsonify(drug_data)
	# drug_list = insert_into_drug_db()
	insert_into_drug_db(drug_data)
	return render_template("drug_submited.html", drug_data=drug_data)

if __name__ == ('__main__'):
	app.run(host='0.0.0.0', debug = True);
