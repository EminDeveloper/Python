from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/helloworld")

@app.route("/helloworld")
def hello_world():
    return "<p>Hello, World from the redirected page!</p>"
    
if __name__ == '__main__':
    app.run(debug=True)
