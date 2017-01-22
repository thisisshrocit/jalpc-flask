#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
# @allow_domain
def hello_world():
    return render_template('index.html')
