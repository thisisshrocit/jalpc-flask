#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify

from . import api
from ..decorators import jsonp, allow_domain
from ..models import JalpcPVCount


@api.route('/jalpc/pv_count')
# @allow_domain
@jsonp
def jalpc_count():
    cnt = JalpcPVCount.access()
    return jsonify(msg='success', data=cnt)
