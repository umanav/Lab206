from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
# PRINT THE RESULTS
# @app.route('/')
# def index():
#     friends = mysql.query_db("SELECT * FROM friends")
#     print friends
#     return render_template('index.html')

# DISPLAY THE RESULTS
@app.route('/')
def index():
    query = "SELECT CONCAT(first_name, ' ',last_name)AS name, age, date_format(since, '%M %d %Y') AS since FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template


@app.route('/friends', methods=['POST'])
def create():
    name = request.form['name']
    f_name = ""
    for i in name:
        if i == " ":
            break
        else:
            f_name +=i
    print f_name;

    # first_name = 
    # last_name =
    query = "INSERT INTO friends (first_name,last_name,age,since, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW(), NOW())"
    # # We'll then create a dictionary of data from the POST data received.
    # data = {
    #          'first_name' : 
    #          'last_name' :
    #          'age': request.form['age']
    #        }
    # # Run query, with dictionary values injected into the query.
    # mysql.query_db(query, data)
    return redirect('/')
    
app.run(debug=True)