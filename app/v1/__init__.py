#! /usr/bin/python3
'''
@Name: __init__.py
@Auth: yingpwu
@Date: 220913-2226
@Desc: 
@Ver : 0.0.0
'''
from flask import Blueprint
from app.v1 import book,user
def create_blueprint():

    bp=Blueprint("v1",__name__,url_prefix="/v1")
    book.book.register(bp)
    user.user.register(bp)
    return bp