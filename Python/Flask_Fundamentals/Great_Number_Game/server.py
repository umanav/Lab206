from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def home():
    if not isinstance(session['random'],int):
        session['random'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route("/guess", methods=['POST'])
def guess():
    print session['random']
    if session['random'] == int(request.form['number']):
        session['result'] = "You guessed"
    elif session['random'] < int(request.form['number']):
        session['result'] = "You guessed too high"
    elif session['random'] > int(request.form['number']):
        session['result'] = "You guessed too low"
    return redirect("/")
app.run(debug=True)