from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/play/')
def play():
    return render_template('play.html', x=int(3))

if __name__=="__main__":
    app.run(debug=True)
