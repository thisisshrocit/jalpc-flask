#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import time

import feedparser
import requests
from flask import jsonify, render_template, request, current_app

from . import api_1_0
from .constant import api_list
from ..decorators import jsonp


@api_1_0.route('/', methods=['GET'])
def index():
    return render_template('api.html', content=api_list)


@api_1_0.route('/time', methods=['GET'])
@jsonp
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
@jsonp
def info():
    app = current_app._get_current_object()
    key = app.config['IP_INFO_DB_KEY']
    ip = request.args.get('ip', None)
    if not ip:
        if request.headers.getlist("X-Forwarded-For"):
            ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            ip = request.remote_addr
        user_agent = {'browser': request.user_agent.browser,
                      'language': request.user_agent.language,
                      'platform': request.user_agent.platform,
                      'string': request.user_agent.string,
                      'version': request.user_agent.version,
                      'status': 'success',
                      'message': 'localhost information'}
    else:
        user_agent = {'status': 'error',
                      'message': 'not query localhost information'}
    ip_info = requests.get('http://api.ipinfodb.com/v3/ip-city/?key={0}&ip={1}&format=json'.format(key, ip)).text
    return jsonify(status='success',
                   data={'ip': ip, 'ip_information': json.loads(ip_info), 'user_agent': user_agent})
