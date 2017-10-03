from flask import Flask, render_template, url_for, request, session, redirect, flash, make_response
from app import app
from flask.ext.pymongo import PyMongo
from werkzeug import secure_filename
import bcrypt, json, requests, bson.binary, os, os.

#connections to the mongo database
#app.config['MONGO_DBNAME'] = ''
#app.config['MONGO_URI'] = ''

#db = PyMongo(app)

#index page
@app.route('/')
def index():
    return render_template('index.html')


if  __name__ == '__main__':
	app.secret_key='mysecret'
	app.run(debug=True)
