from flask import Flask
app = Flask(__name__)

@app.route('/') 
def index(): 
    return '<h1>Hello World!</h1>'

# flask --app hello run
# correct command to run flask app
# refer: https://flask.palletsprojects.com/en/2.3.x/cli/#run-the-development-server