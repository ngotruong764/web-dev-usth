from flask import Flask, render_template, request, redirect, url_for, flash, session

# Create an instance for the class
app = Flask(__name__)
app.secret_key = 'some_secret_key'


# Define the route
@app.route('/home')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contract', methods=['GET', 'POST'])
def contract():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        print(f'Name: {name}, Message: {message}')
        flash(f'Thank you {name}, your message has been received {message}')
    return redirect(url_for('/home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    return


# Dynamic route
@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run(debug=True)
