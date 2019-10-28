# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from flask import Blueprint

from app.libs.redprint import Redprint

__author__ = 'loner'

api = Redprint("book")


@api.route('/get')
def get_book():
    return 'get book'
