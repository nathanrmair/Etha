from app import db

from datetime import datetime as dt

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(80))

    def __init__(self, token):
        self.token = token

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=dt.now())
    src_lat = db.Column(db.Float)
    src_long = db.Column(db.Float)
    dest_lat = db.Column(db.Float)
    dest_long = db.Column(db.Float)

    def __init__(self, src_lat, src_long,
            dest_lat, dest_long, datetime=None):
        self.src_lat = src_lat
        self.src_long = src_long
        self.dest_lat = dest_lat
        self.dest_long = dest_long
        if datetime is not None:
            self.datetime = datetime
