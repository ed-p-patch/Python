from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    value = True
    fl = []
    Firstname = request.form['fname']
    Lastname = request.form['lname']
    Email = request.form['email']
    PassOne = request.form['pass1']
    PassTwo = request.form['pass2']
    
    fl.extend((Firstname, Lastname, Email, PassOne, PassTwo))

    for x in range (0, len(fl)):
        print fl[x]
        if len(fl[x]) < 1:
            value = False
            flash("All fields cannot be empty!")
            break
    if any(Firstname.isdigit() for i in Firstname):
        value = False
        flash("First name cannot contain numbers")
    if any(Lastname.isdigit() for i in Lastname):
        value = False
        flash("Last name cannot contain numbers")
    if len(PassOne) > 9:
        value = False
        flash("Password must be under 8 or less characters")
    if not EMAIL_REGEX.match(Email):
        value = False
        flash("email must be valid example@example.com")
    if PassOne != PassTwo:
        value = False
        flash("Passwords must match")
    if value:
        return render_template('success.html')
    else:
        return redirect('/')
app.run(debug=True)