# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     user
   Description :
   Author :       loner
   date：          2019/10/30
-------------------------------------------------
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

__author__ = 'loner'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(24), index=True, unique=True)
    nickname = db.Column(db.String(24), unique=True)
    type = db.Column(db.Integer)
    __password = db.Column(db.String(100))

    @property
    def set_password(self):
        return self.__password

    @set_password.setter
    def set_password(self, raw):
        self.__password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self.password_hash, raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        user = User()
        user.email = account
        user.set_password = secret
        user.nickname = nickname
        db.session.add(user)
        db.session.commit()
