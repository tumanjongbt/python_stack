from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("user_form.html")

@app.route('/result', methods=['POST'])
def result():
    print("Got Survey Info")
    print(request.form)
    print("Name", request.form['name'])
    print("Location", request.form['location'])
    return render_template("success.html")

@app.route('/danger', methods=['GET'])
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 