import os
basedir = os.path.abspath(os.path.dirname(__file__))
class config(object):

    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('C:\\Users\\jilbe\\Desktop\\Python\\STREAMERSAPI\\database\\streamers.db') or 'sqlite:///' + os.path.join(basedir, 'streamers.db   ')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #ó os.environ.get('DATABASE_URL') 