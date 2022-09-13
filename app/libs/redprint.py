#! /usr/bin/python3
'''
@Name: redprint.py
@Auth: yingpwu
@Date: 220913-2224
@Desc: 
@Ver : 0.0.0
'''
import typing as t


class Redprint():
    def __init__(self, name: str, import_name: str, url_prefix: str):
        self.name = name
        self.url_prefix = url_prefix
        self.mount = []

    def route(self, rule: str, **options: t.Any) -> t.Callable:
        def decorator(f):
            self.mount.append((rule, f, options))
            return f
        return decorator

    def register(self, bp):
        for rule, f, options in self.mount:
            endpoint = options.pop('endpoint', f.__name__)
            bp.add_url_rule(self.url_prefix+rule, endpoint, f, **options)
