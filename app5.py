# Intergating CSS and Javascript in Flask

from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index1.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>= 50:
        res="pass"
    else:
        res="fail"
    exp={'score':score,'result':res}
    return render_template('results.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return'The Person is fail and score is ' + str(score)

@app.route('/submit', methods =['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    res = ""
    # if total_score>=50:
    #     res="success"
    # else:
    #     res="fail"
    return redirect(url_for("success", score=total_score))



if __name__=='__main__':
    app.run(debug=True)