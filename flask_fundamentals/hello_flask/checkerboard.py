from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkerboard.html', x=int(8), y=int(8))

@app.route('/<x>/<y>')
def checkerboard(x=None, y=None):
    return render_template('checkerboard.html', x=int(x), y=int(y)) 
if __name__=="__main__":
    app.run(debug=True) 