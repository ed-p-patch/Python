from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = '1234512345'

@app.route('/')
def index():
    return render_template('index_form.html')

@app.route('/submitted', methods=['POST'])
def result():
    #data = "name: {}, location: {}, language: {}, comment: {}".format(request.form['name'], request.form['location'], request.form['language'], request.form['comment'])
    #data = {"name: {}, location: {}, comment: {}".format(request.form['name'], request.form['location'], request.form['comment'])
    return render_template('index_results.html', name=request.form['name'], location=request.form['location'], comment=request.form['comment'])
    # I struggled finding a correct way to handle drop-down items, as it was creating issues processing.
    # Next, it took me quite awhile to figure out python did not like when I tried to place all data in an object.
app.run(debug=True)