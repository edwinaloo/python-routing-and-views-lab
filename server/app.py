#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)
    return f'The input string is: {input_string}'

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(num + 1))
    return f'Counting from 0 to {num}:\n{numbers}'

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'Result of {num1} {operation} {num2} is: {result}'
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run()

# This Flask application defines four routes:

#     The index() view is mapped to the base URL ("/") and displays an <h1> element with the title of the application.
#     The print_string() view is mapped to the URL pattern "/print/<input_string>" and takes a string as a parameter. It prints the string to the console and displays it in the web browser.
#     The count() view is mapped to the URL pattern "/count/<num>" and takes an integer as a parameter. It generates a string with numbers from 0 to the specified number and displays them on separate lines in the browser.
#     The math() view is mapped to the URL pattern "/math/<num1><operation><num2>" and takes three parameters: num1 (float), operation (string), and num2 (float). It performs the appropriate mathematical operation on the two numbers and displays the result in the browser.

# To run this Flask application, save it in a file (e.g., app.py) and execute python app.py in the terminal. The server will start, and you can access the different views by visiting the corresponding URLs in your web browser.

