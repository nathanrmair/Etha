from app import app, db
from models import Driver, Passenger

import json
import math
from flask import request

DEGREES_TO_RADIANS = math.pi/180.0

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
    passengers = Passenger.query.all()
    passengers_list = [x for x in passengers
            if distance_on_unit_sphere(x.src_lat,x.src_long,x.dest_lat,x.dest_long) < 10]
    y = [{'src_lat': x.src_lat, 'src_long': x.src_long, 'dest_lat': x.dest_lat, 'dest_long': x.dest_long}
            for x in passengers_list]
    return json.dumps(y)

def distance_on_unit_sphere(lat1, long1, lat2, long2):
        # Taken from http://www.johndcook.com/blog/python_longitude_latitude/
        phi1 = (90.0 - lat1) * DEGREES_TO_RADIANS
        phi2 = (90.0 - lat2) * DEGREES_TO_RADIANS

        theta1 = long1 * DEGREES_TO_RADIANS
        theta2 = long2 * DEGREES_TO_RADIANS

        cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2)
                + math.cos(phi1) * math.cos(phi2))
        arc = math.acos(cos)

        return arc * 6373 # Times 6373 for km

