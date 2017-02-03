#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify, request

from . import api_1_0
from ..decorators import jsonp, allow_domain
from ..models import JalpcPVCount


@api_1_0.route('/jalpc/pv_count', methods=['GET'])
# @allow_domain
@jsonp
def jalpc_count():
    cnt = JalpcPVCount.access()
    return jsonify(status='success', data=cnt)
