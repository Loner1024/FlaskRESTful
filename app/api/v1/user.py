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

from app.libs.redprint import Redprint

__author__ = 'loner'

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'I am Loner'
