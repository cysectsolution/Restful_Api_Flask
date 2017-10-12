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


if  __name__ == '__main__':
	app.secret_key='mysecret'
	app.run(debug=True)
