import json
from flask import Flask, Response

JSON_MIME_TYPE = 'application/json'


def success_response(data={}):
    return Response(
        json.dumps({'result': data, 'message': '成功', 'ok': True, 'code': 200}), status=200, mimetype=JSON_MIME_TYPE
    )    
def success_json(data={}):
    return Response(
        json.dumps({'result': data, 'message': '成功', 'ok': True, 'code': 200}), status=200, mimetype=JSON_MIME_TYPE
    )  

def error_response(message, status=400):
    return {'error': None, 'message': message, 'ok': False, 'code': status}, 200, {'Content-Type': JSON_MIME_TYPE}
