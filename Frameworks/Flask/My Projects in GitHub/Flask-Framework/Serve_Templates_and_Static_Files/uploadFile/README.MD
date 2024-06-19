# Flask Framework - Upload File

So when you want to put a file on a website using Python and Flask, it's not too hard. You just need a special type of form in your website's code that says it's okay to send files. Then, on the server side (that's the computer where the website lives), Flask can grab the file from the form you sent and save it in the right place on the server. Easy-peasy!


```bash
pip install flask
```

Okay, to get this going, first, make a new folder called 'file uploading'. Inside that, make two  folder and file: 'templates' and 'main.py'. The 'templates' folder will hold our HTML stuff, and 'main.py' is where we'll put our Python code.

Next up, for the part people see on the website, we need to create an HTML file. This file will let users pick a file from their own computer and then click a button to send it to the website.

**index.html**

```html
<html> 
<head> 
	<title>upload the file : Flask</title> 
</head> 
<body> 
	<form action = "/success" method = "post" enctype="multipart/form-data"> 
		<input type="file" name="file" /> 
		<input type = "submit" value="Upload"> 
	</form> 
</body> 
</html>
```

We must make another HTML file just for acknowledgment. Create a file inside the templates folder called `Acknowledgement.html` to do this. This will only be triggered if the file upload went smoothly. Here, the user will receive a confirmation.

**Acknowledgement.html**

```jinja
<html> 
<head> 
	<title>success</title> 
</head> 
<body> 
	<p>File uploaded successfully</p> 
	<p>File Name: {{name}}</p> 
</body> 
</html>
```

Go to the `main.py` file and type in these codes. This code helps find the name of the file we're working on. After that, we'll save the file we uploaded to the main folder.


