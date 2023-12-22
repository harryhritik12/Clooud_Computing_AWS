from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create a model for personal info
class PersonalInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    school = db.Column(db.String(200), nullable=False)
    college = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    # Fetch the data from the database
    info = PersonalInfo.query.first()
    return render_template('index.html', info=info)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    info = PersonalInfo.query.first()

    if request.method == 'POST':
        info.name = request.form['name']
        info.address = request.form['address']
        info.dob = request.form['dob']
        info.gender = request.form['gender']
        info.age = request.form['age']
        info.school = request.form['school']
        info.college = request.form['college']

        db.session.commit()
        flash('Information updated successfully', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', info=info)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hardcoded username and password for simplicity
        if username == 'admins' and password == '12345678':
            session['loggedin'] = True
            return redirect(url_for('edit'))
        else:
            flash('Incorrect credentials. Try again.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)