from flask import Flask,render_template,request,url_for,redirect
import re

app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template("home.html")
@app.route('/matches',methods=['POST'])
def submit():
    text=request.form.get("test_string")
    reg_exp=request.form.get("regex_string")
    matches = re.findall(reg_exp, text)
    return render_template('result.html',matches=matches)


if __name__=='__main__':
    app.run(debug=True)
