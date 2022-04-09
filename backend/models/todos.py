from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum
import json


class StatusCode(Enum):
    SUCCESS = 0
    FAILED = 1
    ERROR = 2


class Status:
    def __init__(self, statusCode: StatusCode, message: str):
        self.statusCode = statusCode
        self.message = message
    
    def __repr__(self):
        statusStr = ''
        if(self.statusCode == StatusCode.SUCCESS):
            statusStr = 'SUCCESS'
        elif(self.statusCode == StatusCode.FAILED):
            statusStr = 'FAILED'
        elif(self.statusCode == StatusCode.ERROR):
            statusStr = 'ERROR'

        return f'[{statusStr}] {self.message}'


db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        format = '%d/%m/%Y %I:%M:%S %p'
        dc = datetime.strftime(self.date_created, format)
        dm = datetime.strftime(self.date_modified, format)
        return f'[{self.id}] {self.title}: {self.description} - date: [{dm} / {dc}]'


def get_todo(id: int):
    todo = Todo.query.filter_by(id=id).first()
    if todo is None:
        return Status(StatusCode.ERROR, 'not a valid id.')

    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'date_created': todo.date_created,
        'date_modified': todo.date_modified
    }, Status(StatusCode.SUCCESS, 'todo fetched.')

def get_all():
    todos = Todo.query.all()
    return [{
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'date_created': todo.date_created,
        'date_modified': todo.date_modified
    } for todo in todos], Status(StatusCode.SUCCESS, 'all todo fetched')

def create_todo(title: str = None, desc: str = None):
    if title is None and desc is None:
        return Status(StatusCode.ERROR, 'title and desc should not be None.')
    todo = Todo(title=title, description=desc)
    db.session.add(todo)
    db.session.commit()
    
    return Status(StatusCode.SUCCESS, 'todo created.')

def update_todo(id: int, title: str = None, desc: str = None):
    if id is None:
        return Status(StatusCode.ERROR, 'id should not be None.')
    
    if title is None and desc is None:
        return Status(StatusCode.ERROR, 'nothing to update.')

    todo = Todo.query.filter_by(id=id).first()
    if todo is None:
        return Status(StatusCode.FAILED, 'not a valid id.')

    if title is not None:
        todo.title = title
    
    if desc is not None:
        todo.description = desc

    todo.date_modified = datetime.utcnow()
    
    db.session.commit()

    return Status(StatusCode.SUCCESS, 'update successful.')

def delete_todo(id: int):
    if id is None:
        return Status(StatusCode.FAILED, 'id should not be None.')

    todo = Todo.query.filter_by(id=id).first()
    if todo is None:
        return Status(StatusCode.ERROR, 'not a valid id.')
    
    db.session.delete(todo)
    db.session.commit()

    return Status(StatusCode.SUCCESS, 'deletion successful.')

def test(app):

    with app.app_context():
        # todo, status = get_todo(1)
        # print(todo)
        # print(status)

        # print(get_all())

        # print(create_todo('github actions', 'ci/cd'))

        # print(update_todo(4, 'try github actions'))

        # print(delete_todo(4))


        # get all the todos
        # todos = Todo.query.all()
        # print('[')
        # for todo in todos:
        #     print(todo)
        # print(']')

        # get todo with id
        # todo = None if not exists
        todo = Todo.query.filter_by(id=3).first()
        # print(todo)

        # adding a new todo
        # todo = Todo(title='monorepo trial', description='todo web app')
        # db.session.add(todo)
        # db.session.commit()

        # update todo
        # todo = Todo.query.filter_by(id=3).first()
        # todo.title = 'monorepo ci/cd trial'
        # db.session.commit()

        # deleting a todo
        # todo = Todo.query.filter_by(id=3).first()
        # db.session.delete(todo)
        # db.session.commit()

    pass