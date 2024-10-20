# app/helpers/response_helper.py
from flask import jsonify

def create_response(status, data, code):
    if not isinstance(data, list):
        data = [data]
    response = {
        "status": status,
        "data": data,
        "code": code
    }
    return jsonify(response), code

