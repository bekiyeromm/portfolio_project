from flask import Flask,render_template, jsonify
from database import load_users_from_db
# from sqlalchemy import text
# from database import engine
app = Flask(__name__)
	


@app.route('/')
def home():
	user = load_users_from_db()
	return render_template('home.html', jobs = user);

@app.route("/tasks")
def list_of_users():
	pass

@app.route("/logine")
def login():
	return render_template('login.html')


@app.route("/about")
def about():
	return render_template('aboutus.html')


@app.route("/signup")
def signup():
	return render_template('signup.html')


if __name__ == ('__main__'):
	app.run(host='0.0.0.0', debug = True);
