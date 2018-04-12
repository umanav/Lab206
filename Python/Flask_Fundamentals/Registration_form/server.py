from flask import Flask, render_template, request, redirect, session, flash
import re                               
app = Flask(__name__)                     
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    register = True
    #All fields are required and must not be blank
    if len(request.form['email']) < 1 or len(request.form['f_name']) < 1 or len(request.form['l_name']) < 1 or len(request.form['password']) < 1 or len(request.form['c_password']) < 1:
        flash("please fill out all the fields!")
        register = False
    #Password lower than 8
    if len(request.form['password']) < 9:
        flash("Your password has to be more than 8 characters!")
        register = False
    #E-mail not in format
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        register = False
    #different passwords
    if request.form['password'] != request.form['c_password']:
        flash("Your passwords are different")
        register = False
    #First and Last Name cannot contain any numbers
    for letter in request.form['f_name'] or request.form['l_name']:
        if letter.isdigit() == True:
            flash("please only use letters in your name!")
            register = False
            break
    if register:
        flash("success!")
    return redirect('/')
app.run(debug=True) 