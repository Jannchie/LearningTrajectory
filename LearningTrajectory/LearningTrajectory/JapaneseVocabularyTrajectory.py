# coding=utf-8
from LearningTrajectory.database import db

class JapaneseVocabularyTrajectory(db.Model):
    __tablename__ = 'Japanese_vocabulary_trajectory'
    date = db.Column(db.Date, primary_key=True)
    number = db.Column(db.Integer)
    def __init__(self, date, number):
        self.date = date
        self.number = number

