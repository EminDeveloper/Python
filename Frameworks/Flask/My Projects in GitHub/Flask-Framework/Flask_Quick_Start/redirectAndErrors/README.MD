# Flask Framework - Python Flask – Redirect and Errors

## Redirects and Errors Handling in Python Flask

In this article, we're gonna talk about redirects and errors in Python Flask. A redirect in Flask is akin to giving someone directions to go to a specific website. It also comes with a code that tells you what's up.

When we visit a website, our browser communicates with the server, which responds with something called an HTTP status code. It's like a three-number message that informs us about what's happening.

### Reasons for HTTP status codes:

- When someone tries to access without permission or makes a bad request.
- If the website doesn’t support the type of file someone's trying to use.
- At times when the server becomes too busy to handle everything.
- When something inside the server or the connection itself goes awry.

### How to Perform a Redirect in Flask:

```python
flask.redirect(location, code=302)
```


The different  types of HTTP codes are:

| Code | Status             |
|------|--------------------|
| 300  | Multiple_choices   |
| 301  | Moved_permanently  |
| 302  | Found              |
| 303  | See_other          |
| 304  | Not_modified       |
| 305  | Use_proxy          |
| 306  | Reserved           |
| 307  | Temporary_redirect |



**Import the redirect attribute**
We can redirect the URL using Flask by importing redirect. Let’s see how to import redirects from Flask.

```python
from flask import redirect
```

**Example:**

Let’s take a simple example to redirect the URL using a flask named app.py.

```python
# importing redirect 
from flask import Flask, redirect, url_for, render_template, request 

# Initialize the flask application 
app = Flask(__name__) 

# It will load the form template which 
# is in login.html 
@app.route('/') 
def index(): 
	return render_template("login.html") 

@app.route('/success') 
def success(): 
	return "logged in successfully"

# loggnig to the form with method POST or GET 
@app.route("/login", methods=["POST", "GET"]) 
def login(): 
	
	# if the method is POST and Username is admin then 
	# it will redirects to success url. 
	if request.method == "POST" and request.form["username"] == "admin": 
		return redirect(url_for("success")) 

	# if the method is GET or username is not admin, 
	# then it redirects to index method. 
	return redirect(url_for('index')) 


if __name__ == '__main__': 
	app.run(debug=True) 
```


