from flask import Flask,render_template, jsonify,request
from database import load_users_from_db,load_employe_from_db,load_emp_from_db, insert_into_emp_db
app = Flask(__name__)
	


@app.route('/')
def home():
	user = load_users_from_db()
	return render_template('home.html', jobs = user);

 # creating api to retrive the user email and pass as json file
@app.route("/user")
def list_of_users():
	user = load_users_from_db()
	return jsonify(user)

# api to render login.html
@app.route("/login")
def login():
	return render_template('login.html')



@app.route("/signup")
def show_employe():
	emp = load_employe_from_db()
	return render_template('signup.html', users=emp)


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
@app.route("/regg", methods = ['post'])
def register_emp():
	data_from_form = request.form
	# emp = load_emp_from_db()
	insert_into_emp_db(data_from_form)
	return render_template("app_submited.html", form_data=data_from_form)
	


if __name__ == ('__main__'):
	app.run(host='0.0.0.0', debug = True);
