#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import feedparser
import json

from flask import jsonify

from . import api


@api.route('/')
def hello_world():
    return jsonify(result='success', message='Hi there, this is API for Jack.'), 200


@api.route('/time')
def get_time():
    return jsonify(result='success', time=datetime.datetime.now()), 200


@api.route('/rss')
def parse_rss():
    d = feedparser.parse('http://www.jack003.com/feed.xml')
    print d
    print json.dumps(d)
    return 'ok'
