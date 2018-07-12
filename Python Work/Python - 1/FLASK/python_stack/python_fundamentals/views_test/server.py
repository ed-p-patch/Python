from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', phrase="Hello world", times=5)

app.run(debug=True)
