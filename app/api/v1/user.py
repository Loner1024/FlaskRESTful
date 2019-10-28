# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     user
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from flask import Blueprint

__author__ = 'loner'

user = Blueprint('user', __name__)


@user.route('/v1/user/get')
def get_user():
    return 'I am Loner'