from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/play/<x>')
def play(x=None):
    return render_template('play.html', x=int(x)) 

if __name__=="__main__":
    app.run(debug=True) 