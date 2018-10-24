from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsMySecretKey'

@app.route('/start_counter')
def start_counter():
    session['count'] = 1
    return 'New counter started!'

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/add', methods=['POST'])
def add_session():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0    
    return redirect('/')

app.run(debug=True)