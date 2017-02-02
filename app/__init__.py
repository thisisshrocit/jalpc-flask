#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    from .api_1_0 import api_1_0 as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
