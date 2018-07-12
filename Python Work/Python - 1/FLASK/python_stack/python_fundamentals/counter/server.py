from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html", count=session['count'])

@app.route('/by2')
def by_two():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return render_template('index.html', count=session['count'])
    
app.run(debug=True)