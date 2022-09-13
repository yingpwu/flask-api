#! /usr/bin/python3
'''
@Name: ginger.py
@Auth: yingpwu
@Date: 220913-1746
@Desc: 
@Ver : 0.0.0
'''
__author__='yingpwu'
from app.app import create_app


app=create_app()
if __name__ =="__main__":
    app.run(debug=True)