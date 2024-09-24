from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

# flask --app hello run
# correct command to run flask app
# refer: https://flask.palletsprojects.com/en/2.3.x/cli/#run-the-development-server

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

'''
Configure webform
'''
app.config['SECRET_KEY']= 'tdx20020509?'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

'''
App Function Definitions
'''
# view function: handle a web form with GET and POST request methods
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name']= form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())

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