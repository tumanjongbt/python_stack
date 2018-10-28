from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Z][a-zA-Z]*')

app = Flask(__name__)
app.secret_key = "#\xf8'(\xfd\x191J\x0c\xc2-l\xfeN{\x8c"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():

    if len(request.form['email']) < 1:
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

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    elif len(request.form['password']) < 8:
        flash("Password must be more than 8 characters", 'password')

    if len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank!", 'confirm_password')
    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match. Retry", 'confirm_password')
  
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        flash("Thanks for submitting your information")
        return redirect("/")

if __name__=="__main__":
    app.run(debug=True) 


