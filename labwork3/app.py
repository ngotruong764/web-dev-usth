# redirect, url_for: return a redirect from a specific function
# render_template: wrap HTML file and render this
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Create instance of Flask web application
app = Flask(__name__)

# Adding configuration for MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:20092003@localhost:3306/web_dev_2024'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


# Create Students model
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    std_class = db.Column(db.String(80), unique=False, nullable=False)
    mark = db.Column(db.Float, unique=False, nullable=True)

    # Represent object
    def __repr__(self):
        return f'<Student: {self.mark} {self.name} {self.std_class} {self.mark}>'


# with app.app_context():
#     # db.create_all()  # Create the database and table(s)
#
#     # Create new Student objects
#     student1 = Students(name='John Doe', std_class='Math', mark=85.5)
#     student2 = Students(name='Jane Smith', std_class='Science', mark=90.0)
#     student3 = Students(name='Alice Johnson', std_class='History', mark=75.0)
#
#     # Add the objects to the session
#     db.session.add(student1)
#     db.session.add(student2)
#     db.session.add(student3)
#
#     # Commit the session to the database
#     db.session.commit()

# Query all students to verify
# students = Students.query.all()
# print(students)


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


@app.route('/sort')
def sort():
    # get the numbers as a comma-separated string
    numbers_str = request.args.get('numbers', '')
    # split the string into a list of strings
    numbers = numbers_str.split(',')
    # convert the list of strings to a list of integers
    numbers = [int(number) for number in numbers]

    # perform the sorting
    for i in range(len(numbers)):
        # Assume the minimum is the current position
        min_index = i
        for j in range(i + 1, len(numbers)):
            # Update min_index if the element at j is lower than it
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    print(numbers)
    return numbers


@app.route('/reverse_string/<word>')
def reverse_string(word):
    return word[::-1]


@app.route('/create', methods=['GET', 'POST'])
def create():
    student = request.get_json()
    # Get params
    name = student['name']
    std_class = student['std_class']
    mark = student['mark']
    # Create student object
    student = Students(name=name, std_class=std_class, mark=mark)
    # Save to db
    db.session.add(student)
    db.session.commit()

    return 'Successfully created!'


# Get all students which mark < 80 and increase marks to 80
@app.route('/roundMark')
def roundMark():
    # Get student which mark < 80
    students = Students.query.filter(Students.mark < 80).all()
    for student in students:
        student.mark = 80.0
        db.session.add(student)
    db.session.commit()
    return 'Successfully RoundMark!'

@app.route('/displayByGroup')
def displayByGroup():
    # Get students by group
    excellent_std = Students.query.filter(Students.mark > 75).all()
    good_std = Students.query.filter(db.and_(Students.mark >= 60, Students.mark <= 75)).all()
    average_std = Students.query.filter(Students.mark < 60).all()
    # pass variable 'data' to template 'table.html'
    return render_template('display_by_group.html',
                           excellent=excellent_std, good=good_std, average=average_std)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # run the app
