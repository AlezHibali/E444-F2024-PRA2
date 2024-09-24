from flask import Flask, render_template, session, redirect, url_for, flash
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
app.config['SECRET_KEY']= 'SECRET_KEY_SECRET_KEY'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email Address?', validators=[DataRequired()])
    submit = SubmitField('Submit')

'''
App Function Definitions
'''
# view function: handle a web form with GET and POST request methods
# Prevents Duplicate Form Submissions
@app.route('/',methods=['GET','POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name, old_email = session.get('name'), session.get('email')
        # check for flash message
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
            
        session['name']= form.name.data
        session['email']= form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), 
                           email=session.get('email'), current_time=datetime.utcnow())

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