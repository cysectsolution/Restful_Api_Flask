from flask import Flask

app = Flask(__name__)
#importing views from views.py to the server
from app import views