from flask import Flask 

app = Flask(__name__) 

@app.route('/') 
def change_ip_address(): 
	return 'Hey boddy! I changed your ip address. Now this application runing on 183.16.251.236'

if __name__ == '__main__': 
	app.run(host='183.16.251.236') 
