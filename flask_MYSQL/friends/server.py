from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    db = connectToMySQL('friendsdb')
    # now, we may invoke the query_db method
    friend_list = db.query_db("SELECT * FROM friends")
    print("*" * 80)
    print("Fetched all friends", friend_list)
    print("*" * 80)
    return render_template('index.html', friends = friend_list)

@app.route('/process', methods=['POST'])
def add_user():
    print("@" * 80)
    print(request.form)
    print("@" * 80)
    db = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'] 
           }
    db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
