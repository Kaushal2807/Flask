# Flask App Routing

from flask import Flask,render_template,request, redirect, url_for,jsonify

# Create a simple Flask application

app = Flask(__name__)

@app.route("/")
def welcome():
    return"<h1>Hello all welcome!!</h1>"

@app.route("/index")
def index():
    return"<h2>Welcome to the index page !!</h2>"

# Variable Rule

@app.route("/success/<int:scores>")
def success(scores):
    return"The person has passed and the score is : " + str(scores)

@app.route("/fail/<int:scores>")
def fail(scores):
    return"The person has failed and the score is : " + str(scores)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3

        res=""
        if average_marks>= 50:
            res = "success"
        
        else:
            res = "fail"
        return redirect(url_for(res,scores=average_marks))
        # return retrunder_template('form.html',score = average_marks)

@app.route('/api',methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)
    
if __name__ =="__main__":
    app.run(debug=True)