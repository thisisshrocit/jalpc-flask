#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jack vps on vultr'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DOMAIN = ''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite3')
    import logging
    logging.getLogger('flask_cors').level = logging.DEBUG


class ProdConfig(Config):
    DOMAIN = ['jack003', 'jarrekk']
    DEBUG = False
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('/jalpc/db', 'prod.sqlite3')
    import logging
    logging.getLogger('flask_cors').level = logging.DEBUG

config = {
    'default': DevConfig,
    'prod': ProdConfig
}
