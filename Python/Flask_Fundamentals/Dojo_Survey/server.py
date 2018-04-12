from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def display_results():
  name = request.form['name']
  Dojo_Location = request.form['location']
  Favorite_Language = request.form['language']
  Comment = request.form['comment']
  return render_template("results.html", name=name, Dojo_Location=Dojo_Location, Favorite_Language=Favorite_Language, Comment=Comment)
app.run(debug=True) 