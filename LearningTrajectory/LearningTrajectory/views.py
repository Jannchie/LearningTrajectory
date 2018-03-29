"""
Routes and views for the flask application.
"""


from datetime import datetime
from flask import render_template
from LearningTrajectory import app
from LearningTrajectory.database import db
from LearningTrajectory.models.jp import Jp
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Welcome to contact.'
    )

@app.route('/about')
def about():
    """Renders the about page."""

    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Something about me.'
    )

@app.route('/japanese')
def japanese():
    j = Jp.query.all()

    """Renders the japanese page."""
    return render_template(
        'japanese.html',
        data=j,
        title='Japanese Learning Trajectory',
        year=datetime.now().year,
        message='Record my Japanese progress.'
    )
