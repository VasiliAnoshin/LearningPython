from flask import Flask, jsonify
from flask_cors import CORS,cross_origin

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.route('/')
    def hello():
        return jsonify({'message':'HELLO WORLD'})

    @app.after_request
    def after_request(responce):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return responce

    @app.route('/smiley')
    @cross_origin()
    def smiley():
        return ':)'

    return app