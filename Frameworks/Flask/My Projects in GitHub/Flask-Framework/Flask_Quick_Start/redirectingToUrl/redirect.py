from flask import Flask, redirect, url_for

app = Flask(__name__)

# decorator for route(argument) function
@app.route('/admin')
# binding to hello_admin call
def hello_admin():
	return 'Hello Admin'

@app.route('/guest/<guest>')
# binding to hello_guest call
def hello_guest(guest):
	return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):

	# dynamic binding of URL to function
	if name == 'admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest'
								, guest=name))

if __name__ == '__main__':
	app.run(debug=True)
