from flask import jsonify, make_response


def get_success(values, message):
    res = {
        'data': values,
        'message': message,
    }

    return make_response(jsonify(res)), 200

def update_success(data, message):
    res = {
        'id': data,
        'message': message
    }
    return make_response(jsonify(res)), 203

def delete_success(data, message):
    res = {
        'id': data,
        'message': message
    }
    return make_response(jsonify(res)), 204

def post_success(data, message):
    res = {
        'name': data,
        'message': message
    }
    return make_response(jsonify(res)), 201


def bad_request(values, message):
    res = {
        'data': values,
        'message': message,
    }

    return make_response(jsonify(res)), 400

def unauthorized(values, message):
    res = {
        'data': values,
        'message': message,
    }
    
    return make_response(jsonify(res)), 401

def forbidden(values, message):
    res = {
        'data': values,
        'message': message,
    }
    
    return make_response(jsonify(res)), 403

def not_found(message):
    res = {
        'message': message,
    }
    
    return make_response(jsonify(res)), 404