#! /usr/bin/python3
'''
@Name: user.py
@Auth: yingpwu
@Date: 220913-2115
@Desc: 
@Ver : 0.0.0
'''
from app.libs.redprint import Redprint
user=Redprint("user",__name__,url_prefix="/user")

@user.route("/get")
def get_user():
    return "this is a user"