from flask import (
    Flask,
    flash,
    g,
    session,
    redirect,
    render_template,
    request,
)
from flask.ext.mongoengine import MongoEngine

import datetime
import hashlib
import os
import random


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'corgiwrites'}
app.config["SECRET_KEY"] = os.urandom(12)
app.config["DEBUG"] = True

db = MongoEngine(app)

import models

@app.route('/')
def front():
    if user not logged_in:
        return """Welcome to Corgiwrites, your source for corgis and writing."""
    else:
        # redirect to the dashboard

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # display the login form
    else:
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if username is not None and password is not None:
            # look up in the database if the password matches for the username
            user = models.User.objects.get(username=username)
            if user is None:
                # display an error and the login form
                flash.message = "User doesn't exist"
                return redirect('/login')
            if user.password == hashlib.sha256(password).hexdigest():
                # log the user in
                session.is_logged_in = True
                session.username = username
                return redirect('/dashboard')
            else:
                # display an error and the login form
                flash.message = "Wrong password"
                return redirect('/login')
        else:
            # display the login form
            flash.message = 'Both username and password are required'
            return redirect('/login')

@app.route('/logout')
def logout():
    # log the user out
    session.is_logged_in = False
    session.username = None
    return redirect('/')

@app.route('/register')
def register(username, password, email):
    user_exists = database_lookup(username)
    if user_exists is None:
        # start the registration process
        # create a user in the database with the provided username and password and email
        # save the user
        # send them to the login screen
    else:
        # Warn the user that the username is taken and start over

@app.route('/story/create')
def create_story(title, genre, summary):
    if user not logged_in:
        # redirect to the login page
        return
    # save the information to the database
    # send the user to the story page

@app.route('/story/<int:story_id>')
def view_story(story_id):
    if user not logged_in:
        # redirect to the login page
        return
    story = database_lookup(story_id)
    if story is not None:
         # display information about the story
     else:
         # return a 404

@app.route('/story/wordcount/update')
def update_story_wordcount():
    if user not logged_in:
        # redirect to the login page
        return
    pass

@app.route('/market/create')
def create_market(name, url, genre, wordcount):
    if user not logged_in:
        # redirect to the login page
        return
    # save the information to the database
    # send the user to the market page

@app.route('/market/<int:market_id>')
def view_market(market_id):
    if user not logged_in:
        # redirect to the login page
        return
    pass

@app.route('/story/submit')
def submit_story(story_id, market_id):
    if user not logged_in:
        # redirect to the login page
        return
    market = database_lookup(market_id)
    if market is not None:
        # add the story to the market by creating a submission in the database, with the status of 'waiting' and the current date
        # redirect to the story page
    else:
        # provide an error and redirect to the market create page

@app.route('/submission/<int:submission_id>')
def update_submission(submission_id):
    if user not logged_in:
        # redirect to the login page
        return
    # get the submission from the database
    # change the submission status
    # save the submission back to the database
    # redirect to the story page

@app.route('/dashboard')
def dashboard():
    if user not logged_in:
        # redirect to the login page
        return
    # get the current user
    # get the wordcounts by day
    # get the list of stories and submission statuses
    # display a page with all of this information
'''
Actions to do:
* login
* logout
* register
* add story
* update wordcount
* submit story to market
* update submission
* add market
* update market
* dashboard
    * list of stories with statuses
    * daily wordcount
* view story
* view market
'''

if __name__ == '__main__':
    app.run()
