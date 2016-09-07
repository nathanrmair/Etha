from app import app, db
from models import Driver, Passenger

from oauth2client import client, crypt

CLIENT_ID = 'CHANGE ME'

@app.route('/')
def homepage():
    return 'Hello world'

def get_user_from_token(token):
    try:
        #TODO enable token authorization
        #idinfo = verify_id_token(token, CLIENT_ID)
        driver = Driver.query.filter_by(token=token).first()
        if driver:
            return driver
        else:
            driver = Driver(token)
            db.session.add(driver)
            db.session.commit()
            return driver
    except crypt.AppIdentityError:
        return None
