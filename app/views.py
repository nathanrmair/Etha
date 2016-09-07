from app import app

@app.route('/')
def homepage():
    return 'Hello world'
