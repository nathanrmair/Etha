import os
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = False
SECRET_KEY = 'CHANGE_ME'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/testdb.sql'
