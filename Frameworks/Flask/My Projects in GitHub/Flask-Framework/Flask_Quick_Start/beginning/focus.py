from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Good day and good coding, Flask Framework! Focus you mine</p>"
