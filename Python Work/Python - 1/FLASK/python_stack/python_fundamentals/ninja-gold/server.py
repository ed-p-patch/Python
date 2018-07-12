import random
import datetime
from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret123'

def log_event(gold, location):
    now = datetime.datetime.now()
    if gold > 0:
        event_string = 'Earned '+ str(gold) +' golds from the '+ str(location) +'! ('+ str(now) +')'
    else:
        event_string = 'Entered a casino and lost '+ str(gold) +'...Ouch.. ! ('+ str(now) +')'
    return event_string

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'events' not in session:
        session['events'] = []
    return render_template('index.html', gold=session['gold'], events=session['events'])

@app.route('/process_money', methods=['POST', 'GET'])
def get_gold():
    location = request.form['building']
    if location == 'cave':
        new_gold = random.randrange(5, 10)
        session['gold'] += new_gold
        session['events'].append(log_event(new_gold, 'cave'))
    elif location == 'house':
        new_gold = random.randrange(2, 5)
        session['gold'] += new_gold
        session['events'].append(log_event(new_gold, 'house'))
    elif location == 'farm':
        new_gold = random.randrange(10, 20)
        session['gold'] += new_gold
        session['events'].append(log_event(new_gold, 'farm'))
    elif location == 'casino':
        new_gold = random.randint(-50, 50)
        session['gold'] += new_gold
        session['events'].append(log_event(new_gold, 'casino'))
    return redirect('/')

@app.route('/reset')
def reset_god():
    session['events'].pop()
    session['gold'].pop()
    return redirect('/')

app.run(debug=True)