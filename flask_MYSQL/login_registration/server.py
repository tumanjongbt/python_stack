from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_bcrypt import Bcrypt  
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "#\xf8'(\xfd\x191J\x0c\xc2-l\xfeN{\x8c"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/create', methods=['POST'])
def create():

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    if len(request.form['email']) < 3:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')

    if len(request.form['f_name']) < 1:
        flash("First Name cannot be blank!", 'f_name')
    elif not NAME_REGEX.match(request.form['f_name']):
        flash("First Name cannot contain numbers!", 'f_name')

    if len(request.form['l_name']) < 1:
        flash("Last Name cannot be blank!", 'l_name')
    elif not NAME_REGEX.match(request.form['l_name']):
        flash("Last Name cannot contain numbers!", 'l_name')

    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters", 'password')
    if request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match. Retry", 'confirm_password')
  
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        db = connectToMySQL('emaildb')
        unique_query = "SELECT id FROM users WHERE email = %(email)s;"
        unique_data = {
            'email': request.form['email']
        }
        user_list = db.query_db(unique_query, unique_data)
        if len(user_list) > 0:
             flash("Email Address already exist!", 'email')
             return redirect("/")

        hashed_pw = bcrypt.generate_password_hash(request.form['password'])

        db = connectToMySQL('emaildb')
        query = "INSERT INTO users (first_name, last_name, pw_hash, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(pw_hash)s, %(email)s, NOW(), NOW());"
        data = {
            'first_name': request.form['f_name'],
            'last_name':  request.form['l_name'],
            'pw_hash': hashed_pw,
            'email': request.form['email']
        }
        db.query_db(query, data)
        flash("You successfully registered", 'registered')
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    db = connectToMySQL('emaildb')
    login_query = "SELECT pw_hash, id FROM users WHERE email = %(email)s;"
    login_data = {
        'email': request.form['email']
    }
    login_user = db.query_db(login_query, login_data)

    if len(login_user) == 0:
        flash("Email or password incorrect!", 'login')
        return redirect('/')

    user = login_user[0]
    if not bcrypt.check_password_hash(user['pw_hash'], request.form['password']):
         flash("Email or password incorrect!", 'login')
         return redirect('/')
    session['user_id'] = user['id']
    return redirect('/success')

@app.route('/success')
def success():
    if 'user_id' not in session:
        flash("You must be logged in to enter this website!", 'warning')
        return redirect('/')

    db = connectToMySQL('emaildb')
    register_query = "SELECT * FROM users WHERE id=%(user_id)s"
    register_data = {
    'user_id': session['user_id']
    }
    registered_list = db.query_db(register_query, register_data)
    
    user = registered_list[0]
    return render_template('success.html', name=user['first_name'])

@app.route('/logout')
def logout():
        session.pop('user_id', None)
        flash("You have been logged out!", 'logout')
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 





