#! /usr/bin/python3
'''
@Name: book.py
@Auth: yingpwu
@Date: 220913-2121
@Desc: 
@Ver : 0.0.0
'''
from flask import Blueprint
book=Blueprint("book",__name__)

@book.route("/v1/book/get")
def get_book():
    return "this is a book"