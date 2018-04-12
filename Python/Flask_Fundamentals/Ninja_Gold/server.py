from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def home():
    if not isinstance(session['gold'],int):
        session['activities'] = [] 
        session['gold'] = 0
    return render_template("index.html")

@app.route("/process_money", methods=['POST'])
def process_money():
    import time
    ts = time.time()
    time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.form['building'] == 'farm':
        number = random.randrange(10, 21)
        session['gold'] += number
        session['activities'].append("Earned "+str(number)+ " golds from the farm "+"("+ str(time) +")")
    if request.form['building'] == 'cave':
        number = random.randrange(5, 11)
        session['gold'] += number
        session['activities'].append("Earned "+str(number)+ " golds from the cave "+"(" + str(time) + ")")
    if request.form['building'] == 'house':
        number = random.randrange(2, 6)
        session['gold'] += number
        session['activities'].append("Earned "+str(number)+ " golds from the house"+"("+ str(time) +")")
    if request.form['building'] == 'casino':
        number = random.randrange(0, 50)
        option = random.randrange(0, 2)
        if option == 1:
            session['gold'] += number
            session['activities'].append("Earned "+str(number)+ " golds from the casino"+"("+ str(time) +")")
        else:
            session['gold'] -= number
            session['activities'].append("Entered a casino and lost "+str(number)+ " golds"+"("+ str(time) +")")
    return redirect("/")

@app.route("/reset")
def reset():
    session['activities'] = [] 
    session['gold'] = 0
    return redirect("/")
app.run(debug=True)