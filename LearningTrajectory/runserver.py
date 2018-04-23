"""
This script runs the MyLearningPath application using a development server.
"""
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

from os import environ
from LearningTrajectory import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)