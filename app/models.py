#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db


class JalpcPVCount(db.Model):
    __tablename__ = 'jalpcpv'
    count = db.Column(db.Integer, primary_key=True)

    @staticmethod
    def init_db(count=1):
        s = JalpcPVCount(count=count)
        db.session.add(s)
        db.session.commit()
        return s

    @staticmethod
    def access():
        if JalpcPVCount.query.count():
            s = JalpcPVCount.query.first()
            s.count += 1
            db.session.add(s)
            db.session.commit()
            return s.count
        else:
            s = JalpcPVCount.init_db(19000)
            return s.count
