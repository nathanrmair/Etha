#!env/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath('app'))

from app import app
app.run(debug=True)
