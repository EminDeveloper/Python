# [Flask-Framework](https://flask.palletsprojects.com/en/3.0.x/) 

### About Flask Framework:
Flask is a lightweight and flexible web framework for Python. It's designed to be easy to use and build web applications quickly and efficiently. Some of its key features include:

+ **Lightweight**: Flask is simple and easy to get started with.
+ **Modularity**: It allows you to choose the components you need and easily integrate them.
+ **Built-in development server**: Flask comes with a built-in development server, making it convenient for testing your applications.
+ **Extensible**: It provides various extensions to add functionalities as needed.
+ **Jinja2 Templating**: Flask uses the Jinja2 templating engine to render HTML templates.

## Python | Introduction to Web development using Flask

**What is Flask?**
Flask is an API of Python that allows us to build up web-applications. It was developed by Armin Ronacher. Flask’s framework is more explicit than Django’s framework and is also easier to learn because it has less base code to implement a simple web-Application. A Web-Application Framework or Web Framework is the collection of modules and libraries that helps the developer to write applications without writing the low-level codes such as protocols, thread management, etc. Flask is based on WSGI(Web Server Gateway Interface) toolkit and Jinja2 template engine.

**Getting Started With Flask:**
Python 2.6 or higher is required for the installation of the Flask. You can start by import Flask from the flask package on any python IDE. For installation on any environment, you can click on the installation link given below.
To test that if the installation is working, check out this code given below.

### Installing Flask:
To install Flask, you'll need Python installed on your system. Then, you can use pip, Python's package manager, to install Flask. Here are the steps:
1. **Install Python**: If you haven't installed Python, download and install it from the official website: [Python Official Website](https://www.python.org/)
2. **Install Flask**:
Open your terminal or command prompt and enter the following command:

 ```python
 pip install Flask 
 ``` 
### Creating Your First Flask Project:
Once Flask is installed, you can create your first Flask project:
 
**Create a Folder for Your Project:**

Create a new directory for your project. Open your terminal or command prompt, navigate to the directory where you want to create the project, and create a folder, for example:
```bash
mkdir  my_flask_app
my_flask_app
```
**Create a Python File:**
Inside your project folder, create a Python file (e.g., ```app.py```) which will contain your Flask application:
```python
from flask  import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=>True)
```
3. **Run Your Flask Application:**
In the terminal, run your Flask application by executing the Python file you created: python app.py
4. **View Your Application:**
Open a web browser and go to http://127.0.0.1:5000/ or http://localhost:5000/. You should see 'Hello, Flask!' displayed, indicating your Flask app is running.

### Create working enviroment:

#### Install virtual enviroment and add virtual enviroment
```bash
pip install virtualenv
python -m virtualenv venv
source venv/bin/activate # for Linux/MacOS
venv\Scripts\activate 

pip install flask

set FLASK_APP=app.py
flask run
```


Example flask run code:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Good day and good coding, Flask Framework!"
```


‘/’ URL is bound with ```hello()``` function. When the home page of the webserver is opened in the browser, the output of this function will be rendered accordingly.

The Flask application is started by calling the```run()``` function. The method should be restarted manually for any change in the code. To overcome this, the debug support is enabled so as to track any error.

```python
app.debug=True
app.run()
app.run(debug=True) 
```

## Routing [¶](./)

Creating effective routes in web applications is crucial for user engagement. A well-crafted URL not only helps users remember and revisit a page but also enhances their overall experience. Flask simplifies this process by employing the ```route()``` decorator to link a function to a specific URL.
Routing is the process of mapping a URL to a function. 

```python
 from flask 
 import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

### Basic Routing:
In Flask, routing is achieved using the ```@app.route()``` decorator. This decorator binds a URL to a Python function, defining what should be displayed or executed when that URL is accessed.

```python
from flask 
import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```
Here, accessing the root URL (```'/'```) will display 'Index Page', while visiting ```/hello``` will render 'Hello, World'.

### Dynamic Routing:
Flask supports dynamic URLs, allowing parts of the URL to be variable. You can specify variable sections in the route by using ```variable_name```. These variables can then be captured and utilized within the view function.

```python
from flask import Flask

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}' 
```
This route captures any URL with the pattern ```/user/<username>``` and passes the username variable to the ```show_user_profile()``` function.

### URL Building:
Flask provides the ```url_for()``` function to build URLs dynamically based on the endpoint name. This helps avoid hardcoding URLs in the application, making it more maintainable and flexible.

```python
from flask import url_for

@app.route('/profile')
def profile():
    # Assume the function name is 'show_user_profile'
    return url_for('show_user_profile', username='JohnDoe')
```
This ```url_for()``` function generates the URL for the ```show_user_profile()``` function, passing the username as a parameter.

### HTTP Methods and Multiple Routes:
Flask also allows specifying HTTP methods (GET, POST, etc.) for a route. By default, routes only respond to GET requests, but you can explicitly define other methods using the **methods** parameter in the ```@app.route()``` decorator.

```python
@app.route('/submit', methods=['POST'])
def submit_data():
    # Process form data
    pass
```
This route will only handle POST requests sent to **/submit**.

### Grouping Routes:
Flask enables you to group routes using the **Blueprint** feature, allowing for better organization of your application's endpoints. This helps maintain a clear structure as your application grows.

```python
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    # Login logic
    pass

@auth_bp.route('/logout')
def logout():
    # Logout logic
    pass
```
These grouped routes are then registered with the main application.

Understanding and effectively utilizing routing in Flask is key to building well-structured, navigable, and user-friendly web applications.


## Flask – HTTP Method

### Handling HTTP Methods in Flask

This repository explores the implementation of various HTTP methods within Flask using Python. The project focuses on understanding the core concepts of HTTP methods—GET, POST, PUT, PATCH, and DELETE—while demonstrating their usage in Flask applications.

## Core Concepts

### GET
GET requests are utilized to retrieve data from the server. They are commonly used when fetching information from a specified resource.

### POST
POST requests involve submitting data to the server for processing. This method is employed when there's a need to send data to be stored or manipulated on the server.

### PUT
PUT requests are used to modify data on the server. They replace the entire content at a specific location with the data provided in the request body. If the requested resource doesn't exist, a new one is created.

### PATCH
Similar to PUT requests, PATCH requests modify data. However, the key distinction lies in their functionality—they update specific parts of the data, replacing only the content intended for modification.

### DELETE
DELETE requests serve to remove data located at a specified server location. They are instrumental in erasing a resource from the server.

## Implementation

The code within this repository showcases practical examples demonstrating the usage of each HTTP method within Flask. Understanding these methods is fundamental as they form the backbone of data exchange between clients and servers in web development.

Feel free to explore the code and examples provided in this repository to gain a deeper understanding of handling HTTP methods in Flask.

# Understanding HTTP Methods in Client-Server Communication

In a Client-Server architecture, communication between these entities is governed by protocols, defining the rules for seamless interaction. One such fundamental protocol is the Hyper Text Transfer Protocol (HTTP), facilitating communication between clients and servers.

## The Role of HTTP in Client-Server Interaction

Consider the scenario where our browser communicates with a server, like Google, to fetch information. This exchange is made possible through the HTTP. For instance, when we enter a query in our browser, it's transmitted to the Google server, which then processes it and returns relevant suggestions.

## Commonly Used HTTP Methods

### GET
The GET method is a fundamental part of HTTP, primarily used for retrieving data from a server. It is employed when the client needs specific information or resources from the server.

### POST
POST, another vital HTTP method, is used for submitting data to the server. This method is crucial when the client intends to send data to the server for storage or processing.

Understanding these HTTP methods—GET for fetching data and POST for submitting data—forms the core of how clients and servers interact, enabling the seamless exchange of information in the realm of web communication.

Feel free to explore further to gain a deeper understanding of HTTP methods and their role in the Client-Server architecture.


### Example of Using HTTP GET in Flask

This example demonstrates the implementation of the GET method using Flask. We'll create a landing page that provides insights into mathematical calculations and enables users to input a number to retrieve its square.

### Implementation Steps

#### Step 1: Setting Up the HTML Form

Create a file named `square.html` containing a form tag allowing users to input a number. The form's `action` attribute specifies the destination for the form data. As we're utilizing the GET method, the data will be appended to the URL in a name-value pair format.

For instance, if a user enters the number 12 and clicks the Submit button, the data will be appended to the URL in the following format:

http://localhost:5000/square?num=12&btnnum=Submit#

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Square</title>
</head>
<body>
<h1><i> Welcome to the Maths page!</i></h1>
    <p>Logic shapes every choice of our daily lives.<br>
    Logical thinking enables someone to learn and
    make decisions that affect their way of life. !</p>
    <form method="GET" action ="#">
        Enter a number :
        <input type="text" name="num" id="num"></input>
        <input type="submit" name="btnnum" id="btnnum"></input>
  </form>
</body>
</html>
```
#### Step 2: The answer.html code file looks as follows:

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Answer Page!</title>
</head>
<body>
    <h1>Keep Learning Maths!</h1>
    <h2>Square of number {{num}} is :{{squareofnum}}</h2>
</body>
</html>
```

# Handling GET Requests in Flask: A Code Example

### Step 3: Writing the View Function

In this step, we'll create a view function called `squarenumber`. This function serves as a handler for incoming HTTP requests and returns an HTTP response. The function is decorated with `app.route('/square')`, which associates incoming request URLs with specific view functions in Flask.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def squarenumber():
    num = request.args.get('num')
    if num is None:
        return render_template('squarenum.html')
    elif not num.isdigit():
        error_message = 'Please enter a valid number.'
        return render_template('squarenum.html', error=error_message)
    else:
        num = int(num)
        square = num * num
        return render_template('squarenum.html', number=num, result=square)
```

