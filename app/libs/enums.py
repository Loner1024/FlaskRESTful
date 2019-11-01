# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     enums
   Description :
   Author :       loner
   date：          2019/10/30
-------------------------------------------------
"""
from enum import Enum

__author__ = 'loner'


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
