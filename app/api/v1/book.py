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

__author__ = 'loner'

book = Blueprint('book', __name__)


@book.route('/v1/book/get')
def get_book():
    return 'get book'
