# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

__author__ = 'loner'


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object('app.config.secure')
app.config.from_object('app.config.setting')
from app.api.v1 import create_blueprint_v1
app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
