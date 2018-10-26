from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = random.randrange(1, 101)

    if 'display' not in session:
        session['display'] = {
            "content": "Guess a number", 
            "css_class": "start"
        }
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():

    if request.form['userguess'] == "":
        return redirect('/')

    guess = int(request.form['userguess'])
    print("Guess number is", guess)
    
    if guess == session['count']:
       session['display'] = {
           "content": "You guessed correctly",
           "css_class":  "green"
       }

    elif guess > session['count']:
        session['display'] = {
           "content": "Too High",
           "css_class":  "red"
       }
    
    elif guess < session['count']:
        session['display'] = {
           "content": "Too Low",
           "css_class":  "red"
       }

    return render_template("index.html")
    
@app.route('/reset')
def reset():
    session.pop['count']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)