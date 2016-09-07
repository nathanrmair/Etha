from app import app

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



