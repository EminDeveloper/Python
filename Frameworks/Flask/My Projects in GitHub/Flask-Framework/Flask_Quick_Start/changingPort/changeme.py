# import flask module
from flask import Flask

# instance of flask application
app = Flask(__name__)

# home route that returns below text 
# when root url is accessed
@app.route("/")
def change_port():
	return "<p>My Endpoint Port is changed!</p>"

if __name__ == '__main__':
	app.run(debug=True, port=8002)


