from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html")
app.run(debug=True)



# @app.route('/route/with/<vararg>')
# def handler_function(vararg):
#   # here you can use the variable "vararg"
#   # if you want to see what our argument looks like
#   print vararg
#   # we could do other things with this information from this point on such as:
#   # use it to retrieve some records from the database
#   # render a particular template


# You can pass as many variables as you like in the URL as long as they are all passed as parameters to the route handler function:
# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
# 	print username
# 	print id
#     return render_template("user.html")