#coding:utf-8
#config.py
import os

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zlktqa_demo'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

SECRET_KEY = os.urandom(24)