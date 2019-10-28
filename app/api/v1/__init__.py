# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from flask import Blueprint
from app.api.v1 import book, user

__author__ = 'loner'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')
    return bp_v1
