from flask import Flask
#WSGI Application (Web Server Gateway Interface) 
app = Flask(__name__)

@app.route('/')
def welcome():
    return"Welcome to my laptop"

@app.route('/members')
def members():
    return"These are the members of youtube channel please please"

@app.route('/students')
def students():
    return"These are the Students of youtube"

if __name__=='__main__':
    app.run(debug=True)
