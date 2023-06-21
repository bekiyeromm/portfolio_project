from flask import Flask,render_template, jsonify
app = Flask(__name__)
tasks = [
	{
		'id':'1',
		'title':'login',
	},
	{
		'id':'2',
		'title':'sign up',
	}
]

@app.route('/')
def home():
	return render_template('home.html', task = tasks);

@app.route("/tasks")
def list_of_jobs():
	return jsonify(tasks)

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
