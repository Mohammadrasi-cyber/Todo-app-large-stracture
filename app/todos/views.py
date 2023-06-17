from flask import jsonify,request
from app.users.utilities import get_user_by_token,required_login,is_author_object
from .models import Todo
from . import todo

@todo.route('/todos')
def todo_list():
    data, status = required_login(request)
    if not status:
        return jsonify(data)
    user = get_user_by_token(data)
    todo_list = Todo.query.filter_by(author=user.id).all()
    return jsonify({ 'todos': [todo.to_json() for todo in todo_list] })
    
@todo.route('/todos/<pk>/',methods=['PUT'])
def todo_edit(pk):
    data, status = required_login(request)
    if not status:
        return jsonify(data)
    todo = Todo.query.filter_by(id=pk).first()
    is_author,msg = is_author_object(get_user_by_token(data),todo.author)
    if is_author:
        result = todo.from_json_update(request.json)
        return jsonify({'todo':result.to_json()})
    else:
        return jsonify(msg),401
    
@todo.route('/create/todo/',methods=['POST'])
def todo_create():
    data, status = required_login(request)
    if not status:
        return jsonify(data)
    
    
    author=get_user_by_token(request.authorization.token)
    result=Todo.from_json_create(request.json,author.id)
    return jsonify({'todo':result.to_json()})
