from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def home():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template("index.html")

@app.route("/reset")
def reset():
    session['visits'] = 0
    return redirect("/")

@app.route("/add")
def add():
    session['visits']+=1
    return redirect("/")
app.run(debug=True)