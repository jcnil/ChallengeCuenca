#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from libs.models import Base
from libs.configurations import Configuration

class SessionController(object):
    """docstring for SessionController"""
    hostdb = Configuration.DB_HOST
    dbname = Configuration.DB_NAME
    userdb = Configuration.DB_USER
    userpas = Configuration.DB_PASS
    drive = 'postgresql+psycopg2'


    def getEngine(self):
        try:
            access = "%s:%s@%s/%s" % (
                self.userdb, self.userpas, self.hostdb, self.dbname)
            return create_engine("%s://%s" % (self.drive, access))
        except Exception as e:
            raise e


    def getSession(self):
        try:
            engine = self.getEngine()
            DBSession = sessionmaker(bind=engine, autoflush=True)
            session = DBSession()
            return session
        except Exception as e:
            raise e


    def createTables(self):
        try:
            engine = self.getEngine()
            Base.metadata.create_all(engine)
        except Exception as e:
            raise e


    def __init__(self):
        super(SessionController, self).__init__()
