from flask import jsonify

def error_response(error_message, error_code,action,status=None):

    error_response = {
        "action" : action,
        "error_message": error_message,
        "error_code": error_code,
        "status": "rejected" if status == None else status
    }

    return jsonify(error_response), error_code

def success_response(action,status=None,parameter=None,token=None):

    response_data = {
        "action" : action,
        "status": "executed" if status == None else status
    }
    if parameter != None:
        response_data["parameter"] = parameter

    if token != None:
        response_data["token"] = token

    return jsonify(response_data), 200
