from app import app

import json

@app.route('/')
def homepage():
    return 'Hello world'

@app.route('/register')
def homepage2():
    return json.dumps(["status":"OK"])
