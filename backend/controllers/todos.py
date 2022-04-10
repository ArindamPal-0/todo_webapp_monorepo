# create flask blueprint, todo controller
# connect todo controller with todo model

from flask import Blueprint, Response, request
import json
from models.todos import StatusCode
import models.todos as todo_model

api = Blueprint('api', __name__, url_prefix='/api/todos')

@api.route('/', methods=['GET'])
def get_all():
    todos, status = todo_model.get_all()
    response = {
        'message': status.message,
        'success': status.statusCode == StatusCode.SUCCESS,
        'data': todos
    }

    statusCode = 200
    if status.statusCode == StatusCode.ERROR:
        statusCode = 400
    
    return Response(json.dumps(response), status=statusCode, mimetype='application/json')

@api.route('/<int:id>', methods=['GET'])
def get_todo(id):
    todo, status = todo_model.get_todo(id)
    response = {
        'message': status.message,
        'success': status.statusCode == StatusCode.SUCCESS,
        'data': todo
    }

    statusCode = 200
    if status.statusCode != StatusCode.SUCCESS:
        statusCode = 404
    
    return Response(json.dumps(response), status=statusCode, mimetype='application/json')

@api.route('/', methods=['POST'])
def create_todo():
    title = None
    desc = None
    if 'title' in request.json:
        title = request.json['title']

    if 'desc' in request.json:
        desc = request.json['desc']

    response = {
        'message': 'both title and desc should be passed.',
        'success': False
    }

    statusCode = 400

    if title is None or desc is None:
        pass
    else:
        id, status = todo_model.create_todo(title, desc)

        response['message'] = status.message
        response['success'] = status.statusCode == StatusCode.SUCCESS

        if status.statusCode == StatusCode.SUCCESS:
            statusCode = 200
            response['data'] = {'id': id}
    
    return Response(json.dumps(response), status=statusCode, mimetype='application/json')

@api.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    title = None
    desc = None

    if 'title' in request.json:
        title = request.json['title']

    if 'desc' in request.json:
        desc = request.json['desc']

    status = todo_model.update_todo(id, title, desc)

    statusCode = 200
    response = {
        'success': status.statusCode == StatusCode.SUCCESS,
        'message': status.message
    }

    if status.statusCode == StatusCode.ERROR:
        statusCode = 400
    elif status.statusCode == StatusCode.FAILED:
        statusCode = 404

    return Response(json.dumps(response), status=statusCode, mimetype='application/json')

@api.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    status = todo_model.delete_todo(id)

    statusCode = 200
    response = {
        'success': status.statusCode == StatusCode.SUCCESS,
        'message': status.message
    }

    if status.statusCode == StatusCode.ERROR:
        statusCode = 400
    elif status.statusCode == StatusCode.FAILED:
        statusCode = 404

    return Response(json.dumps(response), status=statusCode, mimetype='application/json')
