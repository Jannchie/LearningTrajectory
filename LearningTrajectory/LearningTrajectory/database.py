from LearningTrajectory import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://x:x@1x/x'
db = SQLAlchemy(app)
