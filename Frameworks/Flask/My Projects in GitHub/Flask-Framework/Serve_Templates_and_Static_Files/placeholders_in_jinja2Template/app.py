# app.py 

# import Template from jinja2 for passing the content 
from jinja2 import Template 

# variables that contain placeholder data 
name = 'Mike'
email = 'mike@example.com'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# Create one external form_template html page and read it 
File = open('index_template.html', 'r') 
content = File.read() 
File.close() 

# Render the template and pass the variables 
template = Template(content) 
rendered_form = template.render(pl_name=name, 
								pl_email=email, numbers=numbers) 


# save the txt file in the form.html 
output = open('index.html', 'w') 
output.write(rendered_form) 
output.close() 
