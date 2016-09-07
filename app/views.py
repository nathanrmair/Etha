from app import app, db
from models import Driver, Passenger

import json
from flask import request

@app.route('/')
def homepage():
    return 'Hello world'

@app.route('/register',methods=['POST'])
def register():
    d=json.loads(request.data.decode('utf-8'))
    auth_token = d['auth_token']
    return json.dumps(
        auth_token
    )

@app.route('/passenger',methods=['POST'])
def passenger():
    d=json.loads(request.data.decode('utf-8'))
    dest = (d['dest']['lat'], d['dest']['lng'])
    src = (d['src']['lat'],d['src']['lng'])
    p = Passenger(src[0],src[1],
            dest[0],dest[1])
    db.session.add(p)
    db.session.commit()
    return json.dumps(
	    {
	        "status": "OK"
	    }
    )

@app.route('/update',methods=['POST'])
def update():
    return json.dumps(
	    {
	        "status": "OK"
	    }
    )



