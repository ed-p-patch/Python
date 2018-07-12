import random
from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'won' not in session:
        session['won'] = False
    if session['won'] == True:
        return render_template('/index_won.html', ab='show', int=session['rand'])        
    else:
        if 'rand' not in session:
            session['rand'] = random.randrange(0, 101)
            print 'Number is', session['rand']
        return render_template('index.html')

@app.route('/guess/<num>')
def check_num(num):
    if num == session['rand']:
        session['won'] = true
        return render_template('/index_won.html', pic='justright.jpg', int=num)
    else:
        if num > session['rand']:
            return render_template('index.html', pic='toohigh')
        if num < session['rand']:
            return render_template('index.html', pic='toolow')

@app.route('/play_again')
def reset():
    session['won'] = False
    session['rand'].pop
    return redirect('/')

app.run(debug=True)
