# coding=utf-8
"""
Routes and views for the flask application.
"""


from datetime import datetime
from flask import render_template
from LearningTrajectory import app
from LearningTrajectory.database import db
from LearningTrajectory.JapaneseVocabularyTrajectory import JapaneseVocabularyTrajectory
import json

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='主页',
        year=datetime.now().year,)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='联系',
        year=datetime.now().year,
        message='如果需要联系我')

@app.route('/about')
def about():
    """Renders the about page."""

    return render_template('about.html',
        title='关于',
        year=datetime.now().year,
        message='我想说的一些话')

@app.route('/japanese')
def japanese():
    """Renders the japanese page."""
    return render_template('japanese.html',

        title='日语学习轨迹',
        year=datetime.now().year,
        message='记录下我日语学习的进程')

@app.route('/japaneseGraph')
def japaneseGraph():
    """Renders the japanese page."""
    japaneseVocabularyTrajectory = JapaneseVocabularyTrajectory.query.all()
    data = []
    for row in japaneseVocabularyTrajectory:
        data.append([row.date.strftime("%Y/%m/%d"),row.number])
    return json.dumps(data)