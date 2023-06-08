from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "djfljdfljfnkjsfhjfshjkfjfjfhjdhfdjhdfu"

userpass = "mysql+pymysql://root:@"
basedir = "127.0.0.1"
dbname = "/company"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Employes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, phone, gender, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.address = address

@app.route('/', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        address = request.form['address']

        employee = Employes(name=name, email=email, phone=phone, gender=gender, address=address)
        db.session.add(employee)
        db.session.commit()

        flash('Data added successfully!')
        return redirect(url_for('input_data'))

    return render_template('input.html')

@app.route('/employee_list')
def employee_list():
    employees = Employes.query.all()
    return render_template('index.html', employees=employees)

# @app.route('/edit_data')
# def employee_list():
   
#     return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
