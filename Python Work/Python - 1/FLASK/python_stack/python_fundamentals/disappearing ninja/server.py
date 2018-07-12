from flask import Flask, render_template, redirect, request
app = Flask(__name__)
d = {'blue': 'leonardo', 'purple': 'donatello', 'orange': 'michelangelo', 'red': 'raphael','other': 'notapril', 'all': 'tmnt'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('turtles.html', item=d['all'])

@app.route('/ninja/<color>', methods=['POST', 'GET'])
def single_ninja(color):
    if color.lower() not in d:
        april = d['other']
        return render_template('turtles.html', item=april)
    else:
        turtle = d[color.lower()]
        return render_template('turtles.html', item=turtle)
app.run(debug=True)
        # Seems to fail when I get to specific turtles, Not sure why.  Everything looks good to me.
