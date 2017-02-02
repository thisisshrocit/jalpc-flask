#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import time

import feedparser
from flask import jsonify, render_template, request

from . import api_1_0
from ..decorators import jsonp


@api_1_0.route('/', methods=['GET'])
def index():
    with open('app/api_1_0/api.json') as f:
        content = json.loads(f.read())
    return render_template('api.html', content=content)


@api_1_0.route('/time', methods=['GET'])
def get_time():
    return jsonify(status='success', data=datetime.datetime.now())


@api_1_0.route('/rss', methods=['GET'])
@jsonp
def parse_rss():
    url = request.args.get('url', None)
    if url:
        feed = feedparser.parse(url)
        return jsonify(status='success', data=json.loads(json.dumps(feed, default=lambda obj: time.strftime('%Y-%m-%d %H:%M:%S', obj) if isinstance(obj, time.struct_time) else None)))
    else:
        return jsonify(status='error', data='needs url parameter'), 400
