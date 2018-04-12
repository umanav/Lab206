from flask import Flask, request, redirect, render_template, session, flash
import re  
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify', methods=['POST'])
def verify():
    verified = True
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        verified = False
        return render_template("index.html",verified=verified)
    if verified:
        data = {
             'email' : request.form['email']
             }
        f_query = "INSERT INTO email (email,created_at,updated_at) values (:email,NOW(), NOW())"
        s_query = "SELECT email, created_at FROM email"                           
        insert = mysql.query_db(f_query,data) 
        emails = mysql.query_db(s_query)   
        return render_template('success.html', all_emails=emails, email=email)
    
app.run(debug=True)