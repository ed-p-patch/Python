from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/update_friend', methods=['POST'])
def update():
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': request.form['u_id']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<fid>', methods=['POST'])
def delete(fid):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': fid}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)