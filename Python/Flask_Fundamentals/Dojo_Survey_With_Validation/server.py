from flask import Flask, render_template, request, redirect, session, flash
import re                               
app = Flask(__name__)                     
app.secret_key = 'ThisIsSecret' 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def display_results():
  if len(request.form['name']) > 0 and len(request.form['comment']) > 0:
    session["name"] = request.form['name']
    session["location"] = request.form['location']
    session["language"] = request.form['language']
    session["comment"] = request.form['comment']
    return render_template("results.html")
  else:
    if len(request.form['name']) < 1 and len(request.form['comment']) < 1:
      flash("name and comment cannot be blank!")
    elif len(request.form['name']) < 1:
      flash("name cannot be blank!")
    elif len(request.form['comment']) < 1:
      flash("comment cannot be blank!")
    elif len(request.form['comment']) > 121:
      flash("comment cannot contain more than 120 characters!")
    return redirect('/')
app.run(debug=True) 