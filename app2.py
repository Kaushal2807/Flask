# Building Url Dynamically 
# Variable Rule and URL Building

from flask import Flask, redirect , url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return'Welcome All'

@app.route('/success/<int:score>')
def success(score):
    return'The Person is passed and score is ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return'The Person is fail and score is ' + str(score)

# Result Checker

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if(marks<40):
        result = 'fail' 
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

@app.route('/html')
def html():
    return '<html><body><h1>This is an Html Page<h1><body><html>'


if __name__ == "__main__":
    app.run(debug = True)

