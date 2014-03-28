from app import app

@app.route('/')
def index():
    return "Hello, CW14 again!"
