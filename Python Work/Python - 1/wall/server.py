from flask import Flask, request, redirect, render_template, session, flash
import re, md5
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
app.secret_key = 'super secret key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def check_form(form):
    form_set = True
    if form['pass1'] != form['pass2']:
        flash("Please match password")
        form_set = False
    if len(form['pass1']) < 8:
        flash("Password must be at least 8 characters")
        form_set = False
    if(len(form['fname']) == '') or (len(form['lname']) == ''):
        flash("Please enter a first and last name")
        form_set = False
    if len(form['email']) < 1:  
        flash("Email cannot be blank!")
        form_set = False
    if not EMAIL_REGEX.match(form['email']):
        flash("Please enter a valid email")
        form_set = False
    return form_set

def create_user(form):
    newUser = {
        "email":form['email'],
        "pass": md5.new(form['pass1']).hexdigest(),
        "firstname":form['fname'],
        "lastname":form['lname']
    }
    q = "SELECT * FROM user WHERE email = :email"
    res = mysql.query_db(q, newUser)
    if not res:
        return insert_user(newUser)
    else:
        return False

def insert_user(user):
    q = "INSERT INTO user (firstname, lastname, email, pass, reg_date) VALUES(:firstname, :lastname, :email, :pass, now())"
    res = mysql.query_db(q, user)
    if res:
        flash("Success! User Registered. Please sign in!")
        return True
    else:
        return False

@app.route('/')
def reg():
    return render_template('login.html')

@app.route('/signup')
def log():
    return render_template('register.html')

@app.route('/home')
def index():
    return '<h1>Success</h1><h2><a href="/">Go back?</a></h2>'

@app.route('/register', methods=['POST'])
def process_form():
    form = check_form(request.form)
    if not form:
        return redirect('/')
    else:
        reg = create_user(request.form)
        if not reg:
            flash("An account with that email is already registered or there is an issue with registration")
            return redirect('/')
        else:
            return redirect('/home')

@app.route('/process_log', methods=['POST'])
def p_log():
    e = request.form['email']
    p = md5.new(request.form['pass']).hexdigest()
    data = { "em": e , "pm": p }
    q = "SELECT EXISTS ( SELECT * FROM user WHERE email = :em AND pass = :pm )"
    res = mysql.query_db(q, data)
    if res:
        flash("Successful Login")
        if "user" not in session:
            session["user"] = []
        if data not in session["user"]:
            session["user"].append(data)
        return redirect("/home")
    else:
        flash("Either that account does not exist, or password is incorrect")
        return redirect('/login')

app.run(debug=True)