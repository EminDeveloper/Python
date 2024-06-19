from flask import Flask, render_template 

# Setting up the application 
app = Flask(__name__) 

# making route 

@app.route('/') 
def home(): 
	return render_template('home.html') 


# running application 
if __name__ == '__main__': 
	app.run(debug=True) 
