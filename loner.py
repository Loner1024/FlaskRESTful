# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     loner.py
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from werkzeug.exceptions import HTTPException

from app import app
from app.libs.error import APIException

__author__ = 'loner'


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(code, msg, error_code)
    else:
        return APIException()


if __name__ == '__main__':
    app.run(debug=True)
