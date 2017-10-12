from flask import Flask, render_template, url_for, request, session, redirect, flash, make_response
from app import app
from flask.ext.pymongo import PyMongo
from werkzeug import secure_filename
import bcrypt, json, requests, bson.binary

#connections to the mongo database
app.config['MONGO_DBNAME'] = 'mongotry'
app.config['MONGO_URI'] = 'mongodb://admin:admin@ds111535.mlab.com:11535/mongotry'

db = PyMongo(app)

#index page
@app.route('/')
def index():
    if 'name' in session:
    	return 'you are logged in as ' + session['name']
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
    	users= db.db.users
		existing_user= users.find_one({'name': request.form['name']})

		 if existing_user is None:
			hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
			users.insert({'name':request.form['name'], 'password':hashpass, 'email':request.form['email']})
			session['name'] = request.form['name']
			return redirect(url_for('index'))
		return 'that name exists'	
    	return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    users = db.db.users
  	login_user = users.find_one({'name': request.form['name']})
	
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8'))==login_user['password'].encode('utf-8'):
      	session ['name']=request.form['name']
     	return redirect(url_for('index'))
  	return 'Invalid name or password'
 	return render_template('login.html')	


if  __name__ == '__main__':
	app.secret_key='mysecret'
	app.run(debug=True)
