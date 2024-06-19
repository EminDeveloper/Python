# First we import flask
from flask import Flask

# initialize flask
app = Flask(__name__)

# Display first simple welcome msg
@app.route('/')
def msg():
	return "Welcome"

# We defined string function
@app.route('/vstring/<name>')
def string(name):
	return "My Name is %s" % name

# we run app debugging mode
app.run(debug=True)
