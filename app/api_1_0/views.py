#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import time

import feedparser
import requests
from flask import jsonify, render_template, request, current_app

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
        # todo remove \n
        return jsonify(status='success', data=json.loads(json.dumps(feed, default=lambda obj: time.strftime(
            '%Y-%m-%d %H:%M:%S', obj) if isinstance(obj, time.struct_time) else None).replace('\n', '')))
    else:
        return jsonify(status='error', data='needs url parameter'), 400


@api_1_0.route('/info')
def info():
    app = current_app._get_current_object()
    key = app.config['IP_INFO_DB_KEY']
    user_agent = request.user_agent
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    ip_info = requests.get('http://api.ipinfodb.com/v3/ip-city/?key={0}&ip={1}&format=json'.format(key, ip)).text
    return jsonify(status='success',
                   data={'ip': ip, 'ip_information': json.loads(ip_info), 'user_agent': {'browser': user_agent.browser,
                                                                                         'language': user_agent.language,
                                                                                         'platform': user_agent.platform,
                                                                                         'string': user_agent.string,
                                                                                         'version': user_agent.version}})
