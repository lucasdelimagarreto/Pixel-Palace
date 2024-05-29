from flask import jsonify

def success_response(action, **kwargs):
    response = {
        "action": action,
        "status": "success",
    }
    response.update(kwargs)
    return jsonify(response), 200

def error_response(action, error_code, error_message):
    response = {
        "action": action,
        "error_code": error_code,
        "error_message": error_message,
        "status": "rejected"
    }
    return jsonify(response), error_code
