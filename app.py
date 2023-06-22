from flask import Flask,render_template, jsonify,request
from database import load_users_from_db,load_employe_from_db
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
	users = load_employe_from_db()
	# return jsonify(users)
	return render_template('userlist.html', users=users)

@app.route("/users/register/",methods =['post'])
def regster():
	data = request.form
	return jsonify(data)


if __name__ == ('__main__'):
	app.run(host='0.0.0.0', debug = True);
