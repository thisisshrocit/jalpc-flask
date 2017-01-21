#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from functools import wraps
from flask import request, current_app, jsonify
import app

app = app.create_app(os.getenv('FLASK_CONFIG') or 'default')
domain_name = app.config['DOMAIN']


def jsonp(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', None)
        rtn = f(*args, **kwargs)
        if isinstance(rtn, tuple):
            content = '{0}({1})'.format(str(callback), rtn[0].data) if callback else rtn[0].data
            status = rtn[1]
        else:
            content = '{0}({1})'.format(str(callback), rtn.data) if callback else rtn.data
            status = 200
        return current_app.response_class(content, mimetype='application/json', status=status)

    return decorated_function


def allow_domain(func=None, domain=domain_name):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(*args, **kwargs):
            referrer = request.headers.get('Referer', '@x@')
            if domain not in referrer:
                return jsonify(msg='Domain is denied.', data=None), 400
            return func(*args, **kwargs)
        return returned_wrapper

    if not func:
        def foo(func):
            return decorator(func)

        return foo
    else:
        return decorator(func)
