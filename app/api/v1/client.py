# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     client
   Description :
   Author :       loner
   date：          2019/10/30
-------------------------------------------------
"""
from flask import request

from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User

__author__ = 'loner'

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm(data=request.json).validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm(data=request.json).validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
