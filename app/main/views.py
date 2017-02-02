#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from . import main


@main.route('/')
# @allow_domain
def hello_world():
    return render_template('index.html')
