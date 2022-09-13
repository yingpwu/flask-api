#! /usr/bin/python3
'''
@Name: app.py
@Auth: yingpwu
@Date: 220913-1748
@Desc: 
@Ver : 0.0.0
'''
from flask import Flask

def register_blueprint(app):
    from app.v1.book import book
    from app.v1.user import user
    Flask.register_blueprint(app,book)
    Flask.register_blueprint(app,user)


def create_app():
    app=Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)
    return app