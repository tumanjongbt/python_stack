from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Notice how the key we are using to access the info corresponds with the names
    # of the inputs from our html form
    # name = request.form['name']
    # email = request.form['email']
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    print(request.__dict__)
    return redirect('/show') # redirects back to the '/' route

@app.route('/show', methods=["GET"])
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])

if __name__=="__main__":
    app.run(debug=True)