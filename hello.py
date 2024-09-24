from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# flask --app hello run
# correct command to run flask app
# refer: https://flask.palletsprojects.com/en/2.3.x/cli/#run-the-development-server

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

# make <name> optional
@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500