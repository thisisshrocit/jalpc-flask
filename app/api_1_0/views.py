#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from flask import jsonify

from . import api
from ..decorators import jsonp, allow_domain
from ..models import JalpcPVCount


@api.route('/')
def hello_world():
    return 'Hello World!'


@api.route('/time')
def get_time():
    return jsonify(time=datetime.datetime.now())


@api.route('/jalpc_count')
@allow_domain
@jsonp
def jalpc_count():
    cnt = JalpcPVCount.access()
    return jsonify(msg='success', data=cnt)
