#! /usr/bin/python3
'''
@Name: user.py
@Auth: yingpwu
@Date: 220913-2115
@Desc: 
@Ver : 0.0.0
'''
from flask import Blueprint
user=Blueprint("user",__name__)

@user.route("/v1/user/get")
def get_user():
    return "this is a user"