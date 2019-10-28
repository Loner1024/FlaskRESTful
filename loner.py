# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     loner.py
   Description :
   Author :       loner
   date：          2019-10-29
-------------------------------------------------
"""
from app.app import create_app

__author__ = 'loner'


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)