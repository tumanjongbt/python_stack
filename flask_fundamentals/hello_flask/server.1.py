from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=3)

@app.route('/')
def index1():
    student_info = (
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    );
    return render_template("index1.html", random_numbers = [3,1,5,7,4], students = student_info)

if __name__=="__main__":
    app.run(debug=True)
