#The user being put into your database:

import md5 # do this at the top of your file where you import modules
@app.route('/users/create', methods=['POST'])
def create_user():
     username = request.form['username']
     email = request.form['email']
     password = md5.new(request.form['password']).hexdigest()
     insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username,
     :email, :password, NOW(), NOW())"
     query_data = { 'username': username, 'email': email, 'password': password }
     mysql.query_db(insert_query, query_data)


#When your user is trying to log in:
password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>

#Salted hashing
salt = '123' #where the value 123 changes randomly
hashed_password = md5(password + salt)

#Generating a salt
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))

#The function called os.urandom() returns a string of bytes. The number of bytes is equal to the parameter provided. 
#This string isn't a normal alphanumeric string, so we turn it into a string using the function b2a_hex(), which will turn the value into a normal alphanumeric string. 
#This new random string will be our salt. The idea is to store this salt during the registration process. Example:
username = request.form['username']
email = request.form['email']
password = request.form['password']
salt =  binascii.b2a_hex(os.urandom(15))
hashed_pw = md5.new(password + salt).hexdigest()
insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at)
     VALUES (:username, :email, :hashed_pw, :salt, NOW(), NOW())"
query_data = { 'username': username, 'email': email, 'hashed_pw': hashed_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)

#authenticate a user's login
email = request.form['email']
password = request.form['password']
user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
query_data = {'email': email}
user = mysql.query_db(user_query, query_data)
if len(user) != 0:
 encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
 if user[0]['password'] == encrypted_password:
  # this means we have a successful login!
 else:
     # invalid password!
else:
  # invalid email!
