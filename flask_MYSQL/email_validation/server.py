from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt  

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[A-Z][a-zA-Z]*')

app = Flask(__name__)

bcrypt = Bcrypt(app)
app.secret_key = "#\xf8'(\xfd\x191J\x0c\xc2-l\xfeN{\x8c"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():

    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank!", 'first_name')
    # elif not NAME_REGEX.match(request.form['first_name']):
    #     flash("First Name cannot contain numbers!", 'first_name')

    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!", 'last_name')
    # elif not NAME_REGEX.match(request.form['last_name']):
    #     flash("Last Name cannot contain numbers!", 'last_name')

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    elif len(request.form['password']) < 8:
        flash("Password must be more than 8 characters", 'password')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        myhash = bcrypt.generate_password_hash(request.form['password'])
        print("*" * 80) 
        print(myhash) 
        print("*" * 80) 

        db = connectToMySQL('emaildb')
        query = "INSERT INTO users (first_name, last_name, pw_hash, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(pw_hash)s, %(email)s, NOW(), NOW());"
        data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'pw_hash': myhash,
            'email': request.form['email']
        }
        db.query_db(query, data)
        flash("Thanks for submitting your information")
        return redirect('/success')

@app.route('/success')
def success():
    db = connectToMySQL('emaildb')
    user_results = db.query_db("SELECT email, created_at FROM users;")
    return render_template('success.html', emails = user_results)


@app.route ('/delete')
def delete(id):
    db = connectToMySQL('emaildb')
    query = "DELETE * FROM users where id= %(id)s;"
    data = {
        'id': request.form['id']
    }
    db.query_db(query, data)
    return redirect('/success')

if __name__=="__main__":
    app.run(debug=True)