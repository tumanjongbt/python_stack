from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    # print("Total Order:", int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple']))
    return render_template("checkout.html", mydate=datetime.now(), total=(int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    