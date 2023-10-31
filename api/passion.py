from flask import Blueprint, jsonify, request  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
passion_api = Blueprint('passion_api', __name__,
                   url_prefix='/api/passion')
api = Api(passion_api)
list = ["numbers", "letters"]

class API (Resource):
    def get(self):
        return jsonify("Backend Data")
    
    def post(self):
        data = request.get_json()
        score = data.get('score')
        
api.add_resource(API, '/')