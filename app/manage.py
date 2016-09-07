#!../env/bin/python
from app import app, db

import sys

USAGE = """Usage: manager.py function

---- Valid functions -----
create_db
"""

class Manager:

    def __init__(self, args):
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        self.args = args

    def process(self):
        if len(self.args) < 2:
            print(USAGE)
            return
        if self.args[1] == 'create_db':
            self.create_db()

    def close(self):
        self.app_context.pop()

    def create_db(self):
        db.create_all()

if __name__=='__main__':
    manager = Manager(sys.argv)
    manager.process()
    manager.close()
