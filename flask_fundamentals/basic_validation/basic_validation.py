from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/process', methods=['Post'])
def process():
  #do some validations here!
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 3:
        flash("Name must be 3+ characters", 'name')
            
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template("success.html")

if __name__=="__main__":
    app.run(debug=True)