# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base
   Description :
   Author :       loner
   date：          2019/10/31
-------------------------------------------------
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'loner'


class BaseForm(Form):
    def __int__(self):
        data = request.json
        super(BaseForm, self).__int__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
