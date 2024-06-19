# first we import flask
from flask import Flask

# Initialize flask function
app = Flask(__name__)

@app.route('/')
def msg():
	return "Hola"

# define float function
@app.route('/vfloat/<float:balance>')
def vfloat(balance):
	return "My Account Balance %f" % balance

# we run our code in debugging mode
app.run(debug=True)
