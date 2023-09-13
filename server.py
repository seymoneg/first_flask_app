from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello World" # return HTML version
    return {"message": "Hello World"} # return JSON version
