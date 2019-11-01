# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     error_code
   Description :
   Author :       loner
   date：          2019/10/31
-------------------------------------------------
"""
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = 'loner'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ClientTypeError(APIException):
    code = 400
    msg = 'Client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid error'
    error_code = 1000
