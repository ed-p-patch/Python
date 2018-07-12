from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
app.secret_key = 'super secret key'

@app.route('/')
def index():
    emails = mysql.query_db("SELECT email, check_time FROM user WHERE check_time != 'null'")
    return render_template('index.html', checked=emails)

@app.route('/check_email/', methods=['POST'])
def process():
    data = { 'em': request.form['mail'] }
    q = "SELECT email FROM user WHERE email = :em"
    res = mysql.query_db(q, data)
    if not res:
        flash("Email is not valid!")
    else:
        pass
        flash("The email you enetered {} is a valid email address! Thank you!".format(request.form['mail']))
        q = "UPDATE user SET check_time = now() WHERE email = :em"
        mysql.query_db(q, data)
    return redirect('/')
app.run(debug=True)