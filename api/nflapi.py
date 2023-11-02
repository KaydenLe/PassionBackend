from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests

passion_api = Blueprint('passion_api', __name__, url_prefix='/api/passion')
api = Api(passion_api)

class API(Resource):
    def get(self):
        sample_data = {
        "passion": "Coding",
        "level": "High"
    }
        return jsonify(sample_data)
api.add_resource(API, '/')
