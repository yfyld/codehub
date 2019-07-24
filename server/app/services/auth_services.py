from app.common import response;
from app.common.database import db_session, init_db
from flask import current_app
from app.models.auth import User
from flask_security.utils import  verify_and_update_password
from flask_security import login_user

import time;

class AuthServices():
  def login(self,username,password):
    security = current_app.extensions['security']
    datastore = security.datastore
    
    user = datastore.find_user(username=username)
    print (time.time())
    if not verify_and_update_password(password, user):
        return {'metacode':401, 'msg':'用户不在在或密码不正确'}
    print (time.time())
    login_user(user)
    print (time.time())
    return user

  def signup(self,username,password):
    security = current_app.extensions['security']
    datastore = security.datastore
    init_db()
    user=datastore.create_user(username=username, password=password)
    db_session.commit()
    return user 