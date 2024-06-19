# Flask Framework - Variable Rule

Hey there! Today, we're talking about Flask in Python. It's a small web framework written in Python. What's cool about it is that it's simple to get started with, and you can make big, complex apps with it later on.

### Variable Rules

Variable rules in Flask help us make dynamic URLs. It's like adding blank spots to the web address that we can fill in later.
We use this funny-looking syntax `<variable-name>` in our code to create these variable rules.
These variables get passed as keywords when we use them with the right function.

#### Different Types of Variables in Flask:

Flask gives us a few types of variables we can use:

- **String:** Takes any text but doesn’t allow slashes.
- **Int:** Only accepts whole numbers like 23.
- **Float:** Like Int, but for numbers with decimals like 23.9.
- **Path:** Can take slashes in the text.
- **Any:** Matches one of the things you provide.
- **UUID:** Takes special kinds of strings.

### Simple Flask Program

Here's a simple code in Flask. First, we bring in Flask, then we start it up using the Flask function. After that, we create a basic message, like saying "Welcome!" Finally, we need to run a command in the terminal to see our code in action, which is `Flask run`.



In Flask, there's something called a **"String Variable."** Here's how it works:

First, we import Flask in our code. Then, we set up Flask by using its function. After that, we create a function for a string. But here's the neat part: we don't have to tell the code it's a string because it already knows!

To see our code in action, we run it in the terminal using `Flask run`. When we want to use our `vstring` function, we type `127.0.0.1:5000/vstring/<name>` in the URL. That's how we make it work!


In Flask, there's a feature called an **"Integer Variable."** Here's how it works:

First, we import Flask into our code. Then, we set up Flask by using its function. After that, we create a function for an integer. But here’s the catch: Flask doesn’t know about integers by default, so we've got to define it ourselves. Once we’ve defined our integer function, we make sure to run the code using `Flask run` in the terminal.

To use the `int` page, we need to type the function name in the URL, followed by the specific integer value we want to work with. That’s how we make it all come together!



In Flask, there's a concept called a **"Float Variable."** Here's how it operates:

Firstly, we import Flask into our code. Then, we set up Flask using its function. After that, we create a function for a float. But here’s the catch: Flask doesn’t recognize floats right away, so we’ve got to define them ourselves. Once we’ve defined our float function, we ensure to run the code using `Flask run` in the terminal.

To utilize the float page, we need to input the function name in the URL and append the specific floating-point value we want to work with. That's how it all comes together!

