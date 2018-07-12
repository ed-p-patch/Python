from flask import Flask, render_template, redirect, request, session, flash
##EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
    value = True
    rf_name = request.form['name']
    rf_location = request.form['location']
    rf_language = request.form['language']
    rf_comment = request.form['comment']
    
    if len(rf_name) < 1:
        flash("Name cannot be empty!")
        value = False
    if len(rf_location) < 1:
        flash("location cannot be empty!")
        value = False
    if len(rf_language) < 1:
        flash("Language cannot be empty")
        value = False
    if len(rf_comment) > 120:
        flash("Comment cant be greater than 120 characters")
        value = False
    if value:
        return render_template('success.html', name=rf_name, location=rf_location, language=rf_language, comment=rf_comment)
    else:
        return redirect('/')
app.run(debug=True)