from flask import jsonify,request
from .utilities import json_login,register_user
from . import user


@user.route('/test',methods=['GET'])
def test_view():
    return jsonify({"messeage":'2'})

@user.route('/login',methods=['POST'])
def login():
    return jsonify(json_login(request.json)) 

@user.route('/register', methods=['POST'])
def register():
    return register_user(request)