# first we import flask
from flask import Flask

# Initialize flask function
app = Flask(__name__)

@app.route('/')
def msg():
	return "Hola"

# define int function
@app.route('/vint/<int:age>')
def vint(age):
	return "I am %d years old " % age

# we run our code in debug mode
app.run(debug=True)
