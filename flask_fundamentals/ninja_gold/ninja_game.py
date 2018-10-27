import random
import datetime
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'MySecretKey'

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    
    if 'activities' not in session:
        session['activities'] = []

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def getMoney():
    if request.form['action'] == 'farm':
        farm_add = random.randrange(9, 21)
        session['total_gold'] += farm_add
        session['activities'].append('Earned ' + str(farm_add) + ' golds from the farm! ' + str(datetime.now().strftime("%Y/%m/%d %I:%M%p")))
    
    if request.form['action'] == 'cave':
        cave_add = random.randrange(4, 11)
        session['total_gold'] +=cave_add
        session['activities'].append('Earned ' + str(cave_add) + ' golds from the cave! ' + str(datetime.now().strftime("%Y/%m/%d %I:%M%p")))
    
    if request.form['action'] == 'house':
        house_add = random.randrange(1, 6)
        session['total_gold'] +=house_add
        session['activities'].append('Earned ' + str(house_add) + ' golds from the house! ' + str(datetime.now().strftime("%Y/%m/%d %I:%M%p")))
    
    if request.form['action'] == 'casino':
        casino_add = random.randint(-50, 50)
        session['total_gold'] += casino_add
        if casino_add < 0:
            session['activities'].append('Entered a casino and lost ' + str(casino_add) + ' golds... Ouch! ' + str(datetime.now().strftime("%Y/%m/%d %I:%M%p")))
        else:
            session['activities'].append('Earned ' + str(casino_add) + ' golds from the' + request.form['action'] + str(datetime.now().strftime("%Y/%m/%d %I:%M%p")))

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['total_gold'] = 0
    session['activities'].clear()

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)