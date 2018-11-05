from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL
import datetime

app = Flask(__name__)
app.secret_key = "#\xf8'(\xfd\x191J\x0c\xc2-l\xfeN{\x8c"

@app.route('/')
def index():
    db = connectToMySQL('lead_gen_business')
    customer_leads = db.query_db("SELECT CONCAT(clients.first_name, '  ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id GROUP BY client_name;")

    return render_template('index.html', customers=customer_leads)

@app.route('/date', methods=['POST'])
def date():
    session['start'] = request.form['start']
    session['end'] = request.form['end']
    
    db = connectToMySQL('lead_gen_business')
    query = "SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id WHERE leads.registered_datetime >= %(start)s AND leads.registered_datetime <= %(end)s GROUP BY client_name;"
    data = {
        'start': request.form['start'],
        'end': request.form['end']
    }
    db.query_db(query, data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)