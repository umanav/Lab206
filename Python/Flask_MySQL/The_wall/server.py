from flask import Flask, request, redirect, render_template, session, flash
import re  
import md5
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'thewall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    try:
        session['user']
        return redirect('/wall')
    except:
        return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    register = True
    #All fields are required and must not be blank
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash("please fill out all the fields!","registration")
        register = False
    #Password lower than 8
    if len(request.form['password']) < 9:
        flash("Your password has to be more than 8 characters!","registration")
        register = False
    #E-mail not in format
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!","registration")
        register = False
    #different passwords
    if request.form['password'] != request.form['confirm_password']:
        flash("Your passwords are different","registration")
        register = False
    #First and Last Name cannot contain any numbers
    for letter in request.form['first_name'] or request.form['last_name']:
        if letter.isdigit() == True:
            flash("please only use letters in your name!","registration")
            register = False
            break
    if register:
        data = {
            'first_name' : request.form['first_name'],
            'last_name': request.form['last_name'],
            'email' : request.form['email'],
            'password' : md5.new(request.form['password']).hexdigest(),
            }
        query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) values (:first_name,:last_name,:email,:password,NOW(), NOW())"
        insert = mysql.query_db(query,data)
        user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
        user = mysql.query_db(user_query, data)
        session['user']= user[0]["id"]
        session['full_name'] = data['first_name'] + " "+ data['last_name']
        session['email'] = data['email']
        flash("THANK YOU! You have been registered, please sign in","registration")
        return redirect('/wall')
    return redirect('/')

@app.route('/logIn', methods=['POST'])
def logIn():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
    query_data = { 'email': email, 'password': password}
    user = mysql.query_db(user_query, query_data)
    if user:
        session['user']= user[0]["id"]
        session['full_name'] = user[0]['first_name']+" "+user[0]['last_name']
        session['email'] = user[0]['email']
        return redirect('/wall')
    else:
        flash("The information entered is incorrect","logIn")
    return redirect('/')

@app.route('/wall')
def wall():
    message_query = "SELECT users.id AS id, CONCAT(users.first_name,' ',users.last_name) AS name, messages.message AS message, date_format(messages.created_at, '%M %d %Y') AS date, messages.id AS message_id FROM messages JOIN users on users.id=messages.user_id ORDER BY messages.created_at DESC"
    my_messages= mysql.query_db(message_query)

    comments_query = "SELECT users.id AS id, CONCAT(users.first_name,' ',users.last_name) AS name, date_format(messages.created_at, '%M %d %Y') AS date, comments.comment AS comment, messages.id AS message_id FROM users JOIN comments on comments.user_id = users.id JOIN messages on comments.message_id = messages.id"
    my_comments=mysql.query_db(comments_query)

    return render_template('wall.html', all_posts=my_messages, my_comments=my_comments)

@app.route('/post_message', methods=['POST'])
def post_message():
    data = {
        'user_id' : session['user'],
        'message' :  request.form['post_message'],
        }
    query = "INSERT INTO messages(user_id,message,created_at,updated_at) VALUES (:user_id,:message,NOW(),NOW())"
    post= mysql.query_db(query,data)
    print post
    return redirect('/wall')

@app.route('/post_comment', methods=['POST'])
def post_comment():
    data = {
        'user_id' : session['user'],
        'message_id' :  request.form['message_id'],
        'comment' :  request.form['post_comment'],
        }
    query = "INSERT INTO comments(user_id,message_id,comment,created_at,updated_at) VALUES (:user_id,:message_id,:comment,NOW(),NOW())"
    post= mysql.query_db(query,data)
    print post
    return redirect('/wall')

@app.route('/logOut')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
