from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends_full')
@app.route('/')
def index():
    query = "SELECT id, CONCAT(first_name, ' ',last_name)AS name , email, date_format(created_at, '%M %d %Y') AS created FROM users"       
    friends = mysql.query_db(query)                           
    return render_template('users.html', all_friends=friends) 

@app.route('/users/new')
def new():
    return render_template('new.html')
    
@app.route('/users/create', methods=['GET'])
def create():
    data = {
        'first_name' : request.form['first_name'] ,
        'last_name' : request.form['last_name'] ,
        'email' : request.form['email'] ,
        }
    query = "INSERT INTO users(first_name, last_name,email,created_at,updated_at) VALUES (:first_name,:last_name,:email,NOW(),NOW())"
    add_to_DB= mysql.query_db(query,data)
    return redirect('/')

# @app.route('/users/<id>', methods=['POST'])
# def show(id):

app.run(debug=True)