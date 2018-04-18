# coding=utf-8
from LearningTrajectory import app
from flask_sqlalchemy import SQLAlchemy
import configparser
import os

# 获取当前路径
curr_dir = os.path.dirname(os.path.realpath(__file__))

"""
    获取日志文件。

    此处由于链接字符串中存在敏感信息，比如密码，用户名，服务器IP地址等，上传到GitHub上时为了保证信息安全，需要一个配置文件来存储之。在gitignore文件中加入此文件。
"""
def getConfig(section,key):
    config = configparser.ConfigParser()

    # 使用os.path.join来屏蔽路径的斜杠，从而兼容Windows和Linux
    config.read(os.path.join(curr_dir,"learningTrajectory.conf"))
    return config.get(section,key)

JVTconnectionstring = getConfig("database","JVTconnectionstring")
app.config['SQLALCHEMY_DATABASE_URI'] = JVTconnectionstring
db = SQLAlchemy(app)

