#!../env/bin/python
from app import app, db
from models import Passenger

import sys

USAGE = """Usage: manager.py function [options]

---- Valid functions -----
create_db
spoof_passenger src_lat src_long dest_lat dest_long
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
        elif self.args[1] == 'create_db':
            self.create_db()
        elif self.args[1] == 'spoof_passenger':
            self.spoof_passenger()
        else:
            print(USAGE)

    def close(self):
        self.app_context.pop()

    def create_db(self):
        db.create_all()

    def spoof_passenger(self):
        if len(self.args) < 6:
            print(USAGE)
            return
        p = Passenger(*self.args[2:])
        db.session.add(p)
        db.session.commit()

if __name__=='__main__':
    manager = Manager(sys.argv)
    manager.process()
    manager.close()
