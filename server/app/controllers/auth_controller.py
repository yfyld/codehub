# -*- coding: utf-8 -*-
import functools, json
from app.common import response;
from flask import flash, redirect, request,current_app
from flask import Blueprint, session, url_for, g
from app.services.auth_services import AuthServices
from flask_security import auth_token_required,roles_required
from app.common.cache import cache_key,cache

auth = Blueprint('auth', __name__, url_prefix='/auth')



auth_services = AuthServices()

@auth.route('/aaa')
@cache.cached(timeout=60 * 3, key_prefix=cache_key)
@auth_token_required
def githubLogin():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    return auth_services.login(username,password)

@auth.route('/test')

def test():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    return auth_services.login(username,password)

@auth.route('/login',methods=['POST'])
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    user=auth_services.login(username,password)
    return response.success_response(user.to_dict())


@auth.route('/signup',methods=['POST'])
def signup():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    user=auth_services.signup(username,password)
    return response.success_response(user.to_dict())