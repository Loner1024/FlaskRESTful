# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     app.py
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from flask import Flask
from flask import Blueprint

__author__ = 'loner'


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprint(app)
    return app
