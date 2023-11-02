from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
import random

passion_api = Blueprint('passion_api', __name__, url_prefix='/api/passion')
api = Api(passion_api)

class API(Resource):
    def get(self):
        return jsonify({"message": "Welcome to the Passion API. Use POST request to calculate passion score."})

    def post(self):
        data = request.get_json()
        if 'input_text' not in data:
            return jsonify({"error": "Missing 'input_text' parameter"}), 400

        input_text = data['input_text']
        passion_score = calculate_passion_score(input_text)
        return jsonify({"passion_score": passion_score})

def calculate_passion_score(text):
    # Dummy passion score calculation, you can replace this with your own logic
    score = random.randint(0, 100)
    return score

api.add_resource(API, '/')
