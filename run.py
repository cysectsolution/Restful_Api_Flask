#calling app from the folder app
from app import app
#running the app
if  __name__ == '__main__':
    app.secret_key='mysecret'
    app.run(debug=True, use_reloader=True, port=5000)