# redirect, url_for: return a redirect from a specific function
# render_template: wrap HTML file and render this
from flask import Flask, redirect, url_for, render_template

# Create instance of Flask web application
app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return '<h1>Home Page</h1>'


@app.route('/welcome')
def welcome():
    return 'Welcome to Flask Development!<br>This is Labwork 3: Flask/MySQL/API'


@app.route('/table')
def table():
    # data of the table
    data = [{'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 19},
            {'name': 'Charlie', 'age': 25}, {'name': 'David', 'age': 24},
            {'name': 'Eve', 'age': 21}]

    # pass variable 'data' to template 'table.html'
    return render_template('table.html', data=data)


@app.route('/factorial/<number>')
def factorial(number):
    result = cal_factorial(int(number))
    return f'Factorial of {number} is {str(result)}'


def cal_factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * cal_factorial(number - 1)

@app.route('/is_prime/<number>')
def is_prime(number):
    # convert number to int
    int_number = int(number)
    if int_number < 2:
        return f'{number} is not a prime number'
    else:
        for i in range(2, int_number):
            if int_number % i == 0:
                return f'{number} is not a prime number'
    return f'{number} is a prime number'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # run the app
