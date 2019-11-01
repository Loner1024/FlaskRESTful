# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     secure
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
import os

__author__ = 'loner'

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'dev'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # 配置数据库路径
SQLALCHEMY_TRACK_MODIFICATIONS = False
