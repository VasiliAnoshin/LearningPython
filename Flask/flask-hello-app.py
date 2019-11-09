from flask import Flask

#standart way for creating a flask application
app = Flask(__name__)

@app.route('/')
#index is a standart name for the route handler that listens for connections 
#to the root route and figures out what to do next
def index():
    return 'Hello World!'