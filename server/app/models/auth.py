from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey
from flask_security import  UserMixin, RoleMixin,SQLAlchemySessionUserDatastore
from app.common.database import db_session,Base
import json

class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('users.id'))
    role_id = Column('role_id', Integer(), ForeignKey('roles.id'))

class Role(Base, RoleMixin):
    __tablename__ = 'roles'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    username = Column(String(255),unique=True)
    password = Column(String(255))
    active = Column(Boolean())
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    def to_dict(self):
        return {
            'username':self.username,
            'active':self.active,
            'roles':self.roles
        }




user_datastore = SQLAlchemySessionUserDatastore(db_session,User, Role)



# class User(db.Model):
#     __tablename__ = 'user'

#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     avatar_url = db.Column(db.String(80), nullable=True)


#     def __init__(self, username, avatar_url):
#         self.username = username
#         self.avatar_url = avatar_url


    # @staticmethod
    # def find_or_create_from_token(access_token):
    #     data = GitHub.get_user_from_token(access_token)

    #     """Find existing user or create new User instance"""
    #     instance = User.query.filter_by(username=data['login']).first()

    #     if not instance:
    #         instance = User(data['login'], data['avatar_url'], data['id'])
    #         db.session.add(instance)
    #         db.session.commit()

    #     return instance

    # def __repr__(self):
    #     return "<User: {}>".format(self.username)