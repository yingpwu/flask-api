#! /usr/bin/python3
'''
@Name: book.py
@Auth: yingpwu
@Date: 220913-2121
@Desc: 
@Ver : 0.0.0
'''

from app.libs.redprint import Redprint

book=Redprint("book",__name__,url_prefix="/book")

@book.route("/get")
def get_book():
    return "this is a book"