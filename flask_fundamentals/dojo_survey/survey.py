from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "#\xf8'(\xfd\x191J\x0c\xc2-l\xfeN{\x8c"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey', methods=['POST'])
def survey():

    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')

    if len(request.form['message']) < 1:
        flash("Comment cannot be blank!", 'message')
    elif len(request.form['message']) > 120:
        flash("Comment must be less than 120 characters", 'message')
            
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template("success.html")

@app.route('/danger', methods=['GET'])
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 