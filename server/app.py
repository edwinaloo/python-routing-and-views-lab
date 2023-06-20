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
    app.run(port=5000)




