from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

DB_HOST = "localhost"
DB_NAME = "company"
DB_USER = ""  # Replace with your MySQL username
DB_PASS = ""  # Replace with your MySQL password

conn = mysql.connector.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

@app.route('/')
def Index():
    cur = conn.cursor(dictionary=True)
    s = "SELECT * FROM students"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('index.html', list_users=list_users)

@app.route('/add_student', methods=['POST'])
def add_student():
    cur = conn.cursor()
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        cur.execute("INSERT INTO students (fname, lname, email) VALUES (%s,%s,%s)", (fname, lname, email))
        conn.commit()
        flash('Student Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_student(id):
    cur = conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM students WHERE id = %s', (id,))
    data = cur.fetchone()
    cur.close()
    return render_template('edit.html', student=data)

@app.route('/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']

        cur = conn.cursor()
        cur.execute("""
            UPDATE students
            SET fname = %s,
                lname = %s,
                email = %s
            WHERE id = %s
        """, (fname, lname, email, id))
        flash('Student Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_student(id):
    cur = conn.cursor()
    cur.execute('DELETE FROM students WHERE id = %s', (id,))
    conn.commit()
    flash('Student Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
